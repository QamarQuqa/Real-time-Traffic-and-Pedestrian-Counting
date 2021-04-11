from flask import Flask, render_template, Response, request, send_file, jsonify, make_response, redirect, url_for
import requests
import cv2
import numpy as np
from video_demo import get_frame
import os

app = Flask(__name__)

youtube_link = 0


def edit_link(new_link):
    global youtube_link
    youtube_link = new_link


@app.route('/')
def index():
    # Video streaming home page.
    return render_template('index.html')


@app.route('/render_feed', methods=["GET", "POST"])
def render_feed():

    edit_link(request.form['youtube_link'])

    # Video streaming home page.
    return render_template('video_feed.html')


@app.route('/video_feed')
def video_feed():

    # Video streaming route. Put this in the src attribute of an img tag.
    return Response(get_frame(youtube_link),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int(os.environ.get('PORT', 8000)))
