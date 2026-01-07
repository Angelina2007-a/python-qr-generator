import qrcode

def generate_qr(data, filename):
    """
    Generates a QR code from the provided data and saves it as an image.
    """
    # Create a QR Code Object
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    
    # Add data to the QR code
    qr.add_data(data)
    qr.make(fit=True)

    # Create an image from the QR Code instance
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Save the image
    img.save(filename)
    print(f"Success! QR code saved as {filename}")

if __name__ == "__main__":
    print("--- Simple QR Code Generator ---")
    user_input = input("Enter the text or URL to convert: ")
    output_name = input("Enter filename to save (e.g., my_code.png): ")
    
    # Ensure filename has extension
    if not output_name.endswith(".png"):
        output_name += ".png"
        
    generate_qr(user_input, output_name)