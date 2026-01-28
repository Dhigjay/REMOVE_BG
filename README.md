# 🖼️ Background Remover with Python

<p align="center">
  <img src="https://media.giphy.com/media/3o7aD2saalBwwftBIY/giphy.gif" width="320" alt="Loading Animation">
</p>

<p align="center">
  A simple and powerful Python-based system to remove image backgrounds automatically using the <strong>withoutbg</strong> library.
</p>

---

## ✨ Features

- Remove background from any image automatically  
- Lightweight and easy to use  
- Works with a single Python file  
- Perfect for beginners and students  

---

## 🚀 How It Works

This system uses the `withoutbg` library to process images and remove their backgrounds in just a few lines of code.  
Follow the steps below carefully to run it on your own computer.

---

## 🛠️ Installation & Setup

### 1️⃣ Install Python  
Download and install Python from the official website:

🔗 https://www.python.org/downloads/

Make sure you download the latest stable version for your operating system.

---

### 2️⃣ Add Python & Pip to Environment Variables  
During installation, **check the option**:

> `Add Python to PATH`

If Python is already installed, manually add:
- `PythonXX`
- `PythonXX\Scripts`

to your system environment variables.

---

### 3️⃣ Verify Installation  
Open your terminal or command prompt and type:

```bash
python --version
pip --version
```
---

### 4️⃣ Install the Library
Run this command in your terminal:

```bash
pip install withoutbg
```

---

### 5️⃣ Create Project Folder
Create a new folder (name it anything you like), for example:

```bash
background_remove.py
```
---

### 6️⃣ Insert the Code
Paste this code into `background_remove.py`

---

### 7️⃣ Add Your Image
Place the image you want to remove the background from in the same folder as `background_remove.py`

---

### 8️⃣ Customize Input & Output
Change:
```bash
result = img.remove_background("vas.jpg")
result.save("output_image.png")
```
`vas.jpg` → name of your input image
`output_vas.png` → name of the result image
You can rename them however you like.

---

### 9️⃣ Run the Program
In the project folder, open terminal and run:
```bash
python background_remove.py
```

---

### 🎯 Result

You will get a new image file with the background removed automatically.
Fast, clean, and ready to use!
