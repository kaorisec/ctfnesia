package main

import (
	"fmt"
	"io"
	"net/http"
	"os"
	"path/filepath"
	"reflect"
	"time"

	"github.com/go-macaron/renders"
	"github.com/go-macaron/session"
	"github.com/nwaples/rardecode"
	"gopkg.in/macaron.v1"
)

func writeNewFile(fileName string, rr *rardecode.Reader, headerMode os.FileMode) {
	fmt.Println(fileName)
	newFile, err := os.Create(fileName)
	defer newFile.Close()

	if err != nil {
		fmt.Println(err)
		return
	}

	fmt.Println(reflect.TypeOf(newFile))

	_, err = io.Copy(newFile, rr)
	if err != nil {
		fmt.Println(err)
		return
	}

	// fmt.Println("Whoa.")
	return
}

func extract(rarName string, destDir string) {
	theRar, err := os.Open(rarName)

	if err != nil {
		fmt.Println(err)
		return
	}

	rr, err := rardecode.NewReader(theRar, "")
	if err != nil {
		fmt.Println(err)
		return
	}
	for {
		header, err := rr.Next()
		if err != nil {
			fmt.Println(err)
			return
		}
		fmt.Println("headerName", header.Name)
		writeNewFile(filepath.Join(destDir, header.Name), rr, header.Mode())
	}
	defer theRar.Close()
}

func main() {
	m := macaron.Classic()
	m.Use(renders.Renderer(
		renders.Options{
			Directory:       "templates",                // Specify what path to load the templates from.
			Extensions:      []string{".tmpl", ".html"}, // Specify extensions to load for templates.
			IndentJSON:      true,                       // Output human readable JSON
			IndentXML:       true,                       // Output human readable XML
			HTMLContentType: "text/html",                // Output XHTML content type instead of default "text/html"
		}))
	m.Use(macaron.Static("public",
		macaron.StaticOptions{
			Prefix:      "public",
			SkipLogging: true,
			IndexFile:   "index.html",
			Expires: func() string {
				return time.Now().Add(24 * 60 * time.Minute).UTC().Format("Mon, 02 Jan 2006 15:04:05 GMT")
			},
		}))
	m.Use(macaron.Static("storage",
		macaron.StaticOptions{
			Prefix:      "storage",
			SkipLogging: true,
			Expires: func() string {
				return time.Now().Add(24 * 60 * time.Minute).UTC().Format("Mon, 02 Jan 2006 15:04:05 GMT")
			},
		}))
	m.Use(macaron.Recovery())
	m.Use(session.Sessioner())

	m.Get("/", func(r renders.Render) {
		r.HTML(200, "pages/index.html", map[string]interface{}{"Title": "Home"})
	})

	m.Post("/upload", func(w http.ResponseWriter, r *http.Request, s session.Store) {
		sessID := s.ID()
		if err := r.ParseMultipartForm(2048); err != nil {
			http.Error(w, err.Error(), http.StatusInternalServerError)
			return
		}

		sender := r.FormValue("sender")
		receiver := r.FormValue("receiver")

		uploadedFile, handler, err := r.FormFile("file")
		if err != nil {
			http.Error(w, err.Error(), http.StatusInternalServerError)
			return
		}
		defer uploadedFile.Close()

		dir, err := os.Getwd()
		if err != nil {
			http.Error(w, err.Error(), http.StatusInternalServerError)
			return
		}

		filename := handler.Filename
		fmt.Println(filename)

		if sender != "" && receiver != "" {
			filename = fmt.Sprintf("%s%s", sender, filepath.Ext(handler.Filename))
		}

		dir = filepath.Join(dir, "storage", "uploads", sessID)

		if _, err := os.Stat(dir); os.IsNotExist(err) {
			os.Mkdir(dir, 0755)
		}

		imgDir := filepath.Join(dir, "graphics")
		etcDir := filepath.Join(dir, "others")

		if _, err := os.Stat(imgDir); os.IsNotExist(err) {
			os.Mkdir(imgDir, 0755)
		}

		if _, err := os.Stat(etcDir); os.IsNotExist(err) {
			os.Mkdir(etcDir, 0755)
		}

		if filepath.Ext(handler.Filename) == ".rar" || filepath.Ext(handler.Filename) == ".zip" {
			fileLocation := filepath.Join(etcDir, filename)
			targetFile, err := os.OpenFile(fileLocation, os.O_WRONLY|os.O_CREATE, 0666)
			if err != nil {
				http.Error(w, err.Error(), http.StatusInternalServerError)
				return
			}
			defer targetFile.Close()

			if _, err := io.Copy(targetFile, uploadedFile); err != nil {
				http.Error(w, err.Error(), http.StatusInternalServerError)
				return
			}

			extract(fileLocation, etcDir)

			err = os.Remove(fileLocation)
			if err != nil {
				fmt.Println(err)
				return
			}

		} else if filepath.Ext(handler.Filename) == ".jpg" || filepath.Ext(handler.Filename) == ".png" {
			fileLocation := filepath.Join(imgDir, filename)
			targetFile, err := os.OpenFile(fileLocation, os.O_WRONLY|os.O_CREATE, 0666)
			if err != nil {
				http.Error(w, err.Error(), http.StatusInternalServerError)
				return
			}
			defer targetFile.Close()

			if _, err := io.Copy(targetFile, uploadedFile); err != nil {
				http.Error(w, err.Error(), http.StatusInternalServerError)
				return
			}
		}

		w.Write([]byte("Done!"))
		// http.Redirect(w, r, newUrl, http.StatusSeeOther)

	})

	m.Run()
}
