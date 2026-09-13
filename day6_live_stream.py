import cv2
import time
from day6_cipher_engine import LearnableCipherEngine
import logs
engine = LearnableCipherEngine(block_size=64)
# Open local camera feed (0 is the default webcam)
cap = cv2.VideoCapture(0)

# Disable buffer to force real-time frame fetching
cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)

while True:
    start_time=time.time()

    # Read frame directly into RAM
    ret, frame = cap.read()
    if not ret:
        break

    # Convert to grayscale for initial PoC
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Encrypt on-the-fly (Zero Plaintext Caching)
    encrypted = engine.encrypt_frame(gray_frame)

    # Calculate throughput (FPS)
    fps = 1.0 / (time.time() - start_time)
    cv2.putText(encrypted, f"FPS: {fps:.1f}", (10, 30), 
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255), 2)
    
    cv2.imshow('Zero-Trust Encrypted Feed', encrypted)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
