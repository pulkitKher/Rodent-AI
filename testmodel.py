from ultralytics import YOLO

# Load trained model
model = YOLO("weights/best.pt")

# Run prediction on image
results = model.predict(
    source=r"C:\Users\BIT\OneDrive\Desktop\Rodent_AI\dataset\image\train\6ef3b84bb5f4d9d0.jpg",
    show=True,
    save=True
)
