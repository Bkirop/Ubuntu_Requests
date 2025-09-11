# 🌍 Ubuntu Image Fetcher

**"I am because we are" --- A mindful way to fetch images from the
web.**

Ubuntu Image Fetcher is a Python tool designed to download images while
embracing the spirit of **Ubuntu**: - **Community**: Connects
respectfully to the global web\
- **Respect**: Handles errors gracefully and validates content\
- **Sharing**: Organizes images for community use\
- **Practicality**: Provides real utility with safety measures

------------------------------------------------------------------------

## ✨ Features

-   ✅ **Interactive mode**: Enter one URL at a time\
-   ✅ **Batch mode**: Provide multiple URLs (comma-separated or
    line-separated)\
-   ✅ **Debug mode**: Detailed logging for developers\
-   ✅ **Safety first**:
    -   Validates URLs (HTTP/HTTPS only)\
    -   Ensures files are images before saving\
    -   Limits file size to 50MB\
    -   Avoids duplicate downloads using MD5 hashes\
-   ✅ **Smart filenames**: Automatically generates safe filenames based
    on URL or content type\
-   ✅ **Graceful error handling** with clear feedback

------------------------------------------------------------------------

## 📦 Installation

1.  Clone this repository:

    ``` bash
    git clone https://github.com/Bkirop/Ubuntu_Requests.git
    cd ubuntu-image-fetcher
    ```

2.  Install dependencies:

    ``` bash
    pip install requests
    ```

------------------------------------------------------------------------

## 🚀 Usage

### Run the program

``` bash
python image_fetcher_script.py
```

You'll be prompted to choose a mode: 1. **Interactive mode** -- Enter
image URLs one by one\
2. **Batch mode** -- Provide multiple URLs at once\
3. **Debug mode** -- Enables detailed logging (choose interactive or
batch afterward)

### Run tests with sample URLs

``` bash
python image_fetcher_script.py --test
```

------------------------------------------------------------------------

## 📖 Examples

### Interactive Mode

    Ubuntu Image Fetcher
    Choose your approach:
    1. Interactive mode (single URLs)
    2. Batch mode (multiple URLs)
    3. Debug mode (with detailed logging)

    Enter your choice (1, 2, or 3): 1
    Welcome to the Ubuntu Image Fetcher
    A tool for mindfully collecting images from the web
    Embodying the spirit: 'I am because we are'

    Please enter the image URL (or 'quit' to exit): https://httpbin.org/image/jpeg
    🌍 Connecting to: https://httpbin.org/image/jpeg
    📄 Content type: image/jpeg
    📏 Size: 0.01MB
    ✓ Successfully fetched: jpeg
    ✓ Image saved to: Fetched_Images/jpeg

### Batch Mode

    Enter your choice (1, 2, or 3): 2

    Batch Mode: Enter URLs separated by commas or one per line
    End with an empty line when done:
    https://httpbin.org/image/png, https://httpbin.org/image/jpeg

------------------------------------------------------------------------

## 🛡️ Safety Notes

-   Only supports **HTTP/HTTPS** URLs\
-   Rejects non-image content types\
-   Limits file size to **50MB**\
-   Prevents duplicate downloads

------------------------------------------------------------------------

## 🧪 Development

If you'd like to contribute, fork the repo and create a pull request.\
Debug mode (`choice = 3`) is especially useful for developers who want
deeper insights.

------------------------------------------------------------------------

## 🙏 Acknowledgment

This project is inspired by the Ubuntu philosophy:\
\> *"I am because we are."*

It is not affiliated with Canonical or the Ubuntu operating system, but
reflects the spirit of mindful, community-driven development.

------------------------------------------------------------------------
