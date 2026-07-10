# 🚀 Flight Delay Predictor - VS Code Setup Guide

## 📋 Prerequisites

✅ **Python 3.12.7** - Already installed  
✅ **Dependencies** - Already installed  
✅ **VS Code** - You need to install this

## 🔧 Step 1: Install Visual Studio Code

1. **Download VS Code**: Go to https://code.visualstudio.com/
2. **Install VS Code**: Run the installer and follow the setup
3. **Install Python Extension**: 
   - Open VS Code
   - Go to Extensions (Ctrl+Shift+X)
   - Search for "Python" by Microsoft
   - Click Install

## 📁 Step 2: Open Project in VS Code

### Option A: From VS Code
1. Open VS Code
2. Go to `File` → `Open Folder`
3. Navigate to your project folder: `C:\Users\SOURABH\Downloads\project`
4. Click `Select Folder`

### Option B: From Command Line
```bash
# Navigate to your project
cd C:\Users\SOURABH\Downloads\project

# Open in VS Code
code .
```

## ⚙️ Step 3: Configure Python Interpreter

1. **Open Command Palette**: Press `Ctrl+Shift+P`
2. **Select Python Interpreter**: Type "Python: Select Interpreter"
3. **Choose Interpreter**: Select the Python 3.12 version
4. **Verify**: You should see the Python version in the bottom status bar

## 🚀 Step 4: Run the Application

### Method 1: Using VS Code Terminal (Recommended)

1. **Open Terminal**: Press `Ctrl+`` (backtick) or go to `Terminal` → `New Terminal`
2. **Run the app**:
   ```bash
   streamlit run app.py
   ```
3. **Access the app**: Open your browser and go to `http://localhost:8501`

### Method 2: Using VS Code Run Configuration

1. **Open Run and Debug**: Press `F5` or go to `Run` → `Start Debugging`
2. **Select Configuration**: Choose "Streamlit App" from the dropdown
3. **Run**: The app will start automatically

### Method 3: Using the Play Button

1. **Open app.py**: Click on `app.py` in the file explorer
2. **Click Play**: Look for the play button (▶️) in the top-right corner
3. **Run**: Click the play button to run the file

## 🎯 Step 5: Verify Everything Works

### Check the Application
- ✅ **Local URL**: `http://localhost:8501`
- ✅ **Network URL**: `http://192.168.1.104:8501`
- ✅ **UI Features**: Modern interface with color-coded predictions
- ✅ **Functionality**: Select routes, dates, and times

### Expected Features
- 🟢 **Low Risk**: < 45% (Likely on time)
- 🟡 **Medium Risk**: 45-65% (Possible delays)  
- 🔴 **High Risk**: > 65% (High chance of delays)

## 🔧 Troubleshooting

### Issue 1: "streamlit command not found"
**Solution**: Use the full path:
```bash
python -m streamlit run app.py
```

### Issue 2: Port already in use
**Solution**: Kill the process or use a different port:
```bash
# Kill process on port 8501
netstat -ano | findstr :8501
taskkill /PID <PID> /F

# Or use different port
streamlit run app.py --server.port 8502
```

### Issue 3: Module not found errors
**Solution**: Reinstall dependencies:
```bash
pip install -r requirements.txt
```

### Issue 4: VS Code doesn't recognize Python
**Solution**: 
1. Press `Ctrl+Shift+P`
2. Type "Python: Select Interpreter"
3. Choose Python 3.12

## 📁 Project Structure in VS Code

```
📁 project/
├── 📄 app.py                      # Main application (open this first)
├── 📄 flight_predictor.py         # ML model class
├── 📄 flight_delay_predictor.pkl  # Trained model
├── 📄 test_data.csv              # Test dataset
├── 📄 requirements.txt           # Dependencies
├── 📄 README.md                 # Documentation
├── 📄 QUICK_START.md            # Quick start guide
├── 📄 VSCODE_SETUP.md           # This file
├── 📁 .vscode/                  # VS Code settings
│   ├── 📄 settings.json         # Workspace settings
│   └── 📄 launch.json           # Debug configurations
└── 📁 docs/                     # Documentation
    └── 📄 deployment-guide.md   # Deployment guide
```

## 🎨 VS Code Extensions (Optional but Recommended)

1. **Python** (Microsoft) - Already mentioned
2. **Python Extension Pack** - Additional Python tools
3. **GitLens** - Enhanced Git integration
4. **Auto Rename Tag** - For HTML/CSS editing
5. **Bracket Pair Colorizer** - Better code readability
6. **Material Icon Theme** - Better file icons

## 🚀 Quick Commands

### Terminal Commands
```bash
# Run the app
streamlit run app.py

# Run with specific port
streamlit run app.py --server.port 8502

# Run with debug info
streamlit run app.py --logger.level debug
```

### VS Code Shortcuts
- `Ctrl+`` - Open/Close Terminal
- `F5` - Start Debugging
- `Ctrl+Shift+P` - Command Palette
- `Ctrl+Shift+X` - Extensions
- `Ctrl+Space` - IntelliSense

## 📞 Support

If you encounter any issues:

1. **Check the terminal output** for error messages
2. **Verify Python interpreter** is selected correctly
3. **Ensure all dependencies** are installed
4. **Check file paths** are correct
5. **Restart VS Code** if needed

## 🎉 Success!

Once everything is working, you should see:
- ✅ VS Code with your project open
- ✅ Terminal showing Streamlit running
- ✅ Browser with the Flight Delay Predictor app
- ✅ Interactive UI with route selection and predictions

**Happy coding! 🛫✨** 