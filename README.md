Takes a directory of Markdown files and build a directory of HTML files.

![image](https://github.com/user-attachments/assets/ae8d2e0b-4d81-4d75-8c5e-eb7799b17402)

The flow of data through the full system is:

  1. Markdown files are in the /content directory. A template.html file is in the root of the project.
  2. The static site generator (the Python code in src/) reads the Markdown files and the template file.
  3. The generator converts the Markdown files to a final HTML file for each page and writes them to the /public directory.
  4. We start the built-in Python HTTP server (a separate program, unrelated to the generator) to serve the contents of the /public directory on http://localhost:8888 (our   
     local machine).
  5. We open a browser and navigate to http://localhost:8888 to view the rendered site.

How the SSG works

  1. Delete everything in the /public directory.
  2. Copy any static assets (HTML template, images, CSS, etc.) to the /public directory.
  3. Generate an HTML file for each Markdown file in the /content directory. For each Markdown file:
  4. Open the file and read its contents.
  5. Split the markdown into "blocks" (e.g. paragraphs, headings, lists, etc.).
  6. Convert each block into a tree of HTMLNode objects. For inline elements (like bold text, links, etc.) we will convert:
  7. Raw markdown -> TextNode -> HTMLNode
  8. Join all the HTMLNode blocks under one large parent HTMLNode for the pages.
  9. Use a recursive to_html() method to convert the HTMLNode and all its nested nodes to a giant HTML string and inject it in the HTML template.
  10. Write the full HTML string to a file for that page in the /public directory.
