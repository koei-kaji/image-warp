from typing import cast

import cv2
import numpy as np
import streamlit as st

from image_warp.use_cases._commons.corner_points import (
    CornerPoints,
)
from image_warp.use_cases.detect_corner_points import (
    DetectCornerPointsInputData,
    DetectCornerPointsInteractor,
    DetectCornerPointsOutputData,
)
from image_warp.use_cases.warp_transform import (
    WarpTransformInputData,
    WarpTransformInteractor,
    WarpTransformOutputData,
)

st.set_page_config(page_title="Dev UI", layout="wide")


uploaded_file = st.file_uploader("Choose an image file", accept_multiple_files=False)

col1, col2 = st.columns([8, 4])

if uploaded_file is not None:
    # choose an image
    bytes_data = uploaded_file.getvalue()
    col1.image(bytes_data)

    # calculate image's width and height
    image_array = np.frombuffer(bytes_data, dtype=np.uint8)
    image = cv2.imdecode(image_array, cv2.IMREAD_COLOR)
    height, width = image.shape[:2]

    # detect edge
    detect_edge_input_data = DetectCornerPointsInputData(
        image_bytes=bytes_data, image_extension="jpg"
    )
    detect_edge_interactor = DetectCornerPointsInteractor()
    detect_edge_output_data = cast(
        DetectCornerPointsOutputData,
        detect_edge_interactor.handle(input_data=detect_edge_input_data),
    )

    # set corner points
    points = {
        f"{point}": {
            "x": (width if point.endswith("right") else 0),
            "y": (height if point.startswith("bottom") else 0),
        }
        for point in ["top_left", "top_right", "bottom_right", "bottom_left"]
    }
    if detect_edge_output_data.corner_points is not None:
        points = detect_edge_output_data.corner_points.model_dump()

    col2_1, col2_2 = col2.columns([1, 1])
    for point, coordinates in points.items():
        points[point]["x"] = col2_1.slider(
            f"x: {point}", min_value=0, max_value=width, value=points[point]["x"]
        )
        points[point]["y"] = col2_2.slider(
            f"y: {point}", min_value=0, max_value=height, value=points[point]["y"]
        )

    # warp perspective
    input_data = WarpTransformInputData(
        image_bytes=bytes_data,
        image_extension="jpg",
        converted_points=CornerPoints(**points),  # type: ignore[arg-type]
    )
    interactor = WarpTransformInteractor()
    output_data = cast(
        WarpTransformOutputData, interactor.handle(input_data=input_data)
    )
    col2.image(output_data.image_bytes)
