import time
import os
import pytest
import argparse


def run_case(now_time=None):
    if now_time:
        now_time = now_time
    else:
        struct_time = time.localtime(time.time())
        now_time = time.strftime("%Y-%m-%d_%H-%M-%S", struct_time)
    rootPath = os.path.abspath(os.path.dirname(__file__)) + "/"
    files_path = rootPath + 'test_case/'
    report_path = rootPath + 'report/reportAllure/'

    report_html = os.path.join(rootPath, "report/reportHtml", now_time)
    if not os.path.exists(report_html):
        os.makedirs(report_html)
    try:
        print("starting execute script")
        pytest.main([files_path, "--alluredir", report_path])
        print("execute script finised")
    except Exception as e:
        print("execute script failed", e)
    try:
        cmd = 'allure generate %s -o %s --clean' % (str(report_path), str(report_html))
        print("starting execute report!")
        os.system(cmd)
        print("report finised!")
    except Exception as e:
        print("Report generation failed, please execute again", e)
        print('Failed to execute the use case. Please check the environment configuration')
        raise

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--now_time", type=str, help="time format---Y-m-d_H-M-S")
    args = parser.parse_args()
    args = vars(args)
    if args['now_time']:
        import_json = str(args['now_time'])
        run_case(import_json)
    else:
        run_case()



