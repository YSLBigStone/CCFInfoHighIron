import sys

print("=== Python ===")
print(f"Python: {sys.version}")

print("\n=== PyTorch ===")
import torch

print(f"PyTorch: {torch.__version__}")
print(f"CUDA available: {torch.cuda.is_available()}")
if torch.cuda.is_available():
    print(f"CUDA version: {torch.version.cuda}")
    print(f"GPU: {torch.cuda.get_device_name(0)}")

print("\n=== Key Dependencies ===")
deps = [
    ("numpy", "numpy"),
    ("torchvision", "torchvision"),
    ("cv2", "opencv-python"),
    ("matplotlib", "matplotlib"),
    ("PIL", "pillow"),
    ("pandas", "pandas"),
    ("seaborn", "seaborn"),
    ("sklearn", "scikit-learn"),
    ("yaml", "pyyaml"),
]
for dep, name in deps:
    try:
        mod = __import__(dep)
        print(f"{name}: {mod.__version__}")
    except ImportError as e:
        print(f"{name}: ERROR - {e}")
    except Exception as e:
        print(f"{name}: {e}")

print("\n=== Ultralytics ===")
try:
    import ultralytics

    print(f"Ultralytics: {ultralytics.__version__}")
except Exception as e:
    print(f"Ultralytics: ERROR - {e}")
