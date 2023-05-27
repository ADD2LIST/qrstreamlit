import streamlit as st

import qrcode

import cv2

def generate_qr_code(data, image_size=200):

    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)

    qr.add_data(data)

    qr.make(fit=True)

    qr_image = qr.make_image(fill_color="black", back_color="white")

    qr_image = qr_image.resize((image_size, image_size))

    return qr_image

def read_qr_code(image):

    detector = cv2.QRCodeDetector()

    data, _ = detector.detectAndDecode(image)

    return data

def main():

    st.title("QR Code Maker and Scanner")

    # User input for the data

    data = st.text_input("Enter the data to encode into QR code")

    # Generate QR code

    if st.button("Generate QR Code"):

        if data:

            qr_image = generate_qr_code(data)

            st.image(qr_image, caption="QR Code", use_column_width=True)

        else:

            st.warning("Please enter the data to encode")

    # QR code scanning

    st.header("QR Code Scanner")

    uploaded_image = st.file_uploader("Upload an image containing a QR code", type=["png", "jpeg", "jpg"])

    if uploaded_image is not None:

        image = cv2.imdecode(np.fromstring(uploaded_image.read(), np.uint8), 1)

        decoded_data = read_qr_code(image)

        if decoded_data:

            st.success(f"Decoded data: {decoded_data}")

        else:

            st.error("No QR code found in the uploaded image.")

if __name__ == "__main__":

    main()

