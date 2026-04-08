# 1. Import necessary functionality
import tkinter as tk
from tkinter import Tk, Text, Frame, Button, messagebox, filedialog
import os


# 2. Create a class
class SimpleNotepad:
    # 3. Initialize the class with all the UI
    def __init__(self, root: Tk) -> None:
        self.root = root
        self.root.title('Seph\'s Notepad')

        # Program's Status
        self.current_file_path = None

        # Create a text widget for entering the content
        self.text_area: Text = Text(self.root, wrap='word')
        self.text_area.pack(expand=True, fill='both')

        # Create a frame to hold the buttons
        self.button_frame: Frame = Frame(self.root)
        self.button_frame.pack()

        # Create and pack the save button
        self.save_button: Button = Button(self.button_frame, text='Save', command=self.save_file)
        self.save_button.pack(side=tk.LEFT)

        # Create and pack the load button
        self.load_button: Button = Button(self.button_frame, text='Load', command=self.load_file)
        self.load_button.pack(side=tk.LEFT)

        self.save_as_button: Button = Button(self.button_frame, text = 'Save as', command=self.save_as_file)
        self.save_as_button.pack(side=tk.LEFT)

    def update_title(self):
        # Update window title based on the active file
        if self.current_file_path:
            # Extract filename from full path using os.path.basename
            file_name = os.path.basename(self.current_file_path)
            self.root.title(f"Seph\'s Notepad - {file_name}")
        
        else:
            self.root.title("Seph\'s Notepad - New File")


    # 4. Create a function that saves files
    def save_file(self) -> None:

        if self.current_file_path:
            try:
                with open(self.current_file_path, 'w') as file:
                    file.write(self.text_area.get(1.0, tk.END))
                print(f'Successfully Updated: {self.current_file_path}')
            except Exception as e:
                messagebox.showerror("Error", f"Could not save file: {e}")
        
        else:
            self.save_as_file()

    # Ask the user where to save the file
    def save_as_file(self) -> None:
        file_path = filedialog.asksaveasfilename(defaultextension='.txt',
                                                 filetypes=[('Text files', '*.txt')])
        
        if file_path:
            self.current_file_path = file_path
            self.save_file()
            self.update_title()


    # 5. Create a function that loads files
    def load_file(self) -> None:
        file_path: str = filedialog.askopenfilename(defaultextension='.txt',
                                                    filetypes=[('Text files', '*.txt')])
        
        if file_path:
            try:
                # 5.5 Load the file
                with open(file_path, 'r') as file:
                    content: str = file.read()
                    self.text_area.delete(1.0, tk.END)  # Clear existing content
                    self.text_area.insert(tk.INSERT, content)  # Insert new content

                self.current_file_path = file_path
                self.update_title()
                print(f'File loaded from: {file_path}')
            
            except Exception as e:
                messagebox.showerror("Error", f"Could not load file: {e}")

    # 6. Create a function that runs the program
    def run(self) -> None:
        self.root.mainloop()


# 7. Create the main entry point
def main() -> None:
    root: Tk = tk.Tk()
    app: SimpleNotepad = SimpleNotepad(root=root)
    app.run()


# 8. Run the script
if __name__ == '__main__':
    main()

