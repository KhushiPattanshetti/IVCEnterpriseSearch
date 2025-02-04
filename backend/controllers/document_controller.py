'''"IVC Ventures International Innovation Pvt Ltd (IVC Ventures) Confidential. 
    No license grant and not for distribution of any nature. All Rights Reserved."'''
import os
from flask import jsonify

UPLOAD_FOLDER = "./documents"

def upload_document(file):
    try:
        if not file:
            return jsonify({"error": "No file provided"}), 400

        os.makedirs(UPLOAD_FOLDER, exist_ok=True)  # Ensure directory exists
        file_path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(file_path)

        return jsonify({"message": f"File {file.filename} uploaded successfully!", "path": file_path}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
