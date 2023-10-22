import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    if req.method == "GET":
        # Return the HTML form
        return func.HttpResponse(render_form(), mimetype="text/html")

    elif req.method == "POST":
        # Process the uploaded file
        audio_file = req.files.get('file')
        if not audio_file:
            return func.HttpResponse("No file uploaded.", status_code=400)

        # ... (We will process the uploaded file here) ...

        # For now, just return a message indicating success
        return func.HttpResponse("File uploaded successfully", status_code=200)

def render_form():
    return """
    <html>
    <body>
    <form action="/api/FileUpload" method="post" enctype="multipart/form-data">
        Select audio to upload:
        <input type="file" name="file" id="file">
        <input type="submit" value="Upload Audio" name="submit">
    </form>
    </body>
    </html>
    """
