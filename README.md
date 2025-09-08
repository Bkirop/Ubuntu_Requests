# Image Fetcher

A simple Python script that downloads images from URLs and organizes them locally, embodying Ubuntu principles of community, respect, sharing, and practicality.

## Overview

This tool allows you to easily fetch images from the web and store them in an organized directory structure. It handles various edge cases gracefully and provides a reliable way to collect images for personal or educational use.

## Features

- 🌐 **Community**: Connects to the wider web to fetch images from any accessible URL
- 🛡️ **Respect**: Handles errors gracefully without crashing, respecting both user experience and server limitations
- 📁 **Sharing**: Organizes fetched images in a dedicated directory for easy access and sharing
- 🔧 **Practicality**: Solves the real need of quickly downloading and organizing images from the web

## Requirements

- Python 3.6 or higher
- `requests` library

## Installation

1. Clone or download this script to your local machine
2. Install the required dependency:

```bash
pip install requests
```

## Usage

Run the script from your terminal:

```bash
python image_fetcher.py
```

The script will:
1. Prompt you to enter an image URL
2. Automatically create a `Fetched_Images` directory if it doesn't exist
3. Download the image from the provided URL
4. Save it with an appropriate filename
5. Provide feedback on the operation status

### Example

```
Enter the image URL: https://example.com/beautiful-sunset.jpg
✓ Image successfully downloaded and saved as: Fetched_Images/beautiful-sunset.jpg
```

## Technical Implementation

### Core Functionality

- **URL Validation**: Checks if the provided URL is accessible
- **HTTP Error Handling**: Properly handles various HTTP status codes (404, 403, 500, etc.)
- **Directory Management**: Uses `os.makedirs()` with `exist_ok=True` to create the storage directory
- **Filename Extraction**: Intelligently extracts filenames from URLs or generates appropriate ones
- **Binary File Handling**: Saves images in binary mode to preserve file integrity

### Error Handling

The script gracefully handles:
- Network connectivity issues
- Invalid URLs
- HTTP errors (4xx, 5xx status codes)
- Permission issues when creating directories or saving files
- Corrupted or incomplete downloads

### File Organization

```
project-directory/
│
├── image_fetcher.py
└── Fetched_Images/
    ├── image1.jpg
    ├── image2.png
    └── ...
```

## Ubuntu Principles Implementation

### 1. Community 🤝
- Connects your local environment to the global web community
- Enables access to shared visual resources across the internet
- Facilitates collaboration by making web images easily accessible locally

### 2. Respect 🙏
- Handles network failures and server errors without crashing
- Provides clear, informative error messages
- Respects server responses and doesn't retry aggressively
- Validates input before making requests

### 3. Sharing 📤
- Organizes downloaded images in a dedicated, shareable directory
- Creates a clean file structure that others can easily understand
- Preserves original filenames when possible for better identification
- Makes collected images ready for distribution or collaborative use

### 4. Practicality 🔨
- Solves the common need of downloading web images quickly
- Requires minimal setup and dependencies
- Provides immediate, tangible value
- Uses standard Python libraries for maximum compatibility

## Error Messages and Troubleshooting

| Error Type | Possible Causes | Solutions |
|------------|----------------|-----------|
| `ConnectionError` | No internet connection, server down | Check internet connection, try again later |
| `HTTP 404` | Image not found | Verify the URL is correct |
| `HTTP 403` | Access forbidden | Image may be protected, try a different source |
| `Permission Error` | Cannot create directory/file | Check write permissions in the current directory |
| `Invalid URL` | Malformed URL | Ensure URL starts with http:// or https:// |

## Supported Image Formats

The script can download any file format, but is optimized for common image types:
- JPEG (.jpg, .jpeg)
- PNG (.png)
- GIF (.gif)
- WebP (.webp)
- SVG (.svg)
- BMP (.bmp)

## Future Enhancements

- [ ] Batch download from multiple URLs
- [ ] Resume interrupted downloads
- [ ] Image format conversion
- [ ] Duplicate detection
- [ ] Progress bar for large downloads
- [ ] Configuration file support

## Contributing

Feel free to contribute improvements, bug fixes, or new features. This project embodies the Ubuntu spirit of community collaboration.

## License

This project is open source and available under the [MIT License](LICENSE).
s
## Support

If you encounter issues or have questions:
1. Check the error messages for guidance
2. Ensure you have the required dependencies installed
3. Verify your internet connection
4. Try with a different image URL to isolate the issue

---

*Built with Ubuntu principles: Community • Respect • Sharing • Practicality*