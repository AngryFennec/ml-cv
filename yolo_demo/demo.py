#! /usr/bin/env python
# coding=utf-8
# ================================================================
#   Copyright (C) 2018 * Ltd. All rights reserved.
#
#   Editor      : VIM
#   File name   : demo.py
#   Author      : YunYang1994
#   Created date: 2018-11-30 15:56:37
#   Description :
#
# ================================================================

import cv2
import numpy as np
import yolo_demo.core.utils as utils
import tensorflow as tf
import os

pth = os.path.abspath(os.path.dirname(__file__)).replace(os.sep, "/")


def start(image_path=pth + "/data/cat.jpg", need_to_show=True):
    return_elements = [
        "input/input_data:0",
        "pred_sbbox/concat_2:0",
        "pred_lbbox/concat_2:0",
    ]
    pb_file = pth + "/yolov3_nano_416.pb"
    num_classes = 20
    input_size = 416
    graph = tf.Graph()
    return_tensors = utils.read_pb_return_tensors(
        graph, pb_file, return_elements
    )
    print("input.name =", return_tensors[0].name)
    print("output1.name =", return_tensors[1].name)
    print("output2.name =", return_tensors[2].name)

    with tf.compat.v1.Session(graph=graph) as sess:
        frame = cv2.imread(image_path, cv2.COLOR_BGR2RGB)
        frame_size = frame.shape[:2]
        image_data = utils.image_preporcess(
            np.copy(frame), [input_size, input_size]
        )
        image_data = image_data[np.newaxis, ...]

        pred_sbbox, pred_lbbox = sess.run(
            [return_tensors[1], return_tensors[2]],
            feed_dict={return_tensors[0]: image_data},
        )

        pred_bbox = np.concatenate(
            [
                np.reshape(pred_sbbox, (-1, 5 + num_classes)),
                np.reshape(pred_lbbox, (-1, 5 + num_classes)),
            ],
            axis=0,
        )

        bboxes = utils.postprocess_boxes(
            pred_bbox, frame_size, input_size, 0.3
        )
        bboxes = utils.nms(bboxes, 0.45, method="nms")
        image = utils.draw_bbox(frame, bboxes)

        result = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        if need_to_show:
            cv2.namedWindow("result", cv2.WINDOW_AUTOSIZE)
            cv2.imshow("result", result)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        return result


start()
