from yolo_demo import demo
import os
import cv2


pth = os.path.abspath(os.path.dirname(__file__)).replace(os.sep, "/")


def test_regress():
    fact_result = demo.start(pth + "/test_data/source.jpg", False)
    plan_result = cv2.imread(pth + "/test_data/result.png", cv2.COLOR_BGR2RGB)
    if (
        plan_result.shape[0] != fact_result.shape[0]
        or plan_result.shape[1] != fact_result.shape[1]
    ):
        assert False
        return
    difference = cv2.subtract(plan_result, fact_result)
    b, g, r = cv2.split(difference)
    assert (
        cv2.countNonZero(b) == 0
        and cv2.countNonZero(g) == 0
        and cv2.countNonZero(r) == 0
    )
