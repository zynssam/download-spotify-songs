import tkinter as tk
from tkinter import messagebox

def create_url_input_app():
    # Initialize a variable to hold the link
    saved_url = None

    # Create the main application window
    root = tk.Tk()
    root.title("URL Input Example")
    root.geometry("400x200")

    # Create a label for instructions
    label = tk.Label(root, text="Enter a URL:")
    label.pack(pady=10)

    # Create an Entry widget for user input
    entry = tk.Entry(root, width=50)
    entry.pack(pady=10)

    # Function to handle button click
    def on_button_click():
        nonlocal saved_url  # Use nonlocal to modify the variable in the outer function
        url = entry.get()  # Get the URL from the entry widget
        if url:
            saved_url = url  # Save the URL to the variable
            messagebox.showinfo("URL Saved", f"You entered: {saved_url}")
            root.quit()  # Exit the main loop
        else:
            messagebox.showwarning("Input Error", "Please enter a valid URL.")

    # Create a button
    button = tk.Button(root, text="Submit", command=on_button_click)
    button.pack(pady=10)

    # Start the Tkinter event loop
    root.mainloop()

    return saved_url  # Return the saved URL after closing the application

if __name__ == "__main__":
    url = create_url_input_app()  # Call the function once
    print(f"The saved URL is: {url}" if url else "No URL was entered.")