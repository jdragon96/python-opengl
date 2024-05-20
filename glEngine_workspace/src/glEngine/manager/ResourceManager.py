import sys
import os

__PROJECT_DIR__  = f"{os.path.dirname(os.path.realpath(__file__))}\\..\\"
__RESOURCE_FOLDER_DIR__ = f"{__PROJECT_DIR__}resource\\" 

# 리소스 경로를 반환
def get_resource_path(res_path: str) -> str:
  return os.path.join(__RESOURCE_FOLDER_DIR__, res_path)

# 리소스 폴더 경로를 반환
def get_resource_folder_dir() -> str:
  return __RESOURCE_FOLDER_DIR__