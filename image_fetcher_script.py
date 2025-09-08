import requests
import os
import hashlib
import mimetypes
from urllib.parse import urlparse
from pathlib import Path

class UbuntuImageFetcher:
    """
    Ubuntu-inspired Image Fetcher: "I am because we are"
    
    This class embodies Ubuntu principles:
    - Community: Connects respectfully to the global web
    - Respect: Handles errors gracefully and validates content
    - Sharing: Organizes images for community use
    - Practicality: Provides real utility with safety measures
    """
    
    def __init__(self, base_dir="Fetched_Images", debug=False):
        self.base_dir = Path(base_dir)
        self.downloaded_hashes = set()
        self.session = requests.Session()
        self.debug = debug
        # Set a respectful User-Agent header
        self.session.headers.update({
            'User-Agent': 'Ubuntu-Image-Fetcher/1.0 (Respectful Community Tool)'
        })
    
    def create_directory(self):
        """Create the base directory with Ubuntu spirit of preparation"""
        try:
            self.base_dir.mkdir(exist_ok=True, parents=True)
            return True
        except Exception as e:
            print(f"✗ Could not create directory: {e}")
            return False
    
    def is_safe_url(self, url):
        """Basic URL safety checks - Ubuntu principle of respect"""
        try:
            parsed = urlparse(url)
            # Check for valid scheme and netloc
            if not parsed.scheme in ['http', 'https']:
                return False, "Only HTTP/HTTPS URLs are supported"
            if not parsed.netloc:
                return False, "Invalid URL format"
            return True, "URL appears safe"
        except Exception as e:
            return False, f"URL validation error: {e}"
    
    def get_content_info(self, response):
        """Extract important information from HTTP headers"""
        content_type = response.headers.get('content-type', '').lower()
        content_length = response.headers.get('content-length')
        
        # Check if it's actually an image
        if not content_type.startswith('image/'):
            return False, f"Content is not an image (type: {content_type})"
        
        # Check file size (limit to 50MB for safety)
        if content_length:
            size_mb = int(content_length) / (1024 * 1024)
            if size_mb > 50:
                return False, f"File too large: {size_mb:.1f}MB (limit: 50MB)"
        
        return True, {
            'content_type': content_type,
            'size': content_length,
            'content_disposition': response.headers.get('content-disposition')
        }
    
    def generate_filename(self, url, content_type):
        """Generate appropriate filename from URL or content type"""
        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path)
        
        # If no filename in URL, generate one
        if not filename or '.' not in filename:
            # Get extension from content type
            extension = mimetypes.guess_extension(content_type) or '.jpg'
            filename = f"ubuntu_image_{hash(url) % 10000}{extension}"
        
        # Sanitize filename for safety
        filename = "".join(c for c in filename if c.isalnum() or c in '.-_').rstrip()
        
        return filename
    
    def calculate_hash(self, content):
        """Calculate hash to prevent duplicates - Ubuntu sharing principle"""
        return hashlib.md5(content).hexdigest()
    
    def fetch_single_image(self, url):
        """Fetch a single image with full Ubuntu principles implementation"""
        print(f"\n🌍 Connecting to: {url}")
        
        # Safety check
        is_safe, safety_msg = self.is_safe_url(url)
        if not is_safe:
            print(f"✗ Safety check failed: {safety_msg}")
            return False
        
        try:
            # Make the request with timeout and proper headers
            response = self.session.get(url, timeout=10, stream=True)
            response.raise_for_status()
            
            # Check content information
            is_valid, content_info = self.get_content_info(response)
            if not is_valid:
                print(f"✗ Content validation failed: {content_info}")
                return False
            
            print(f"📄 Content type: {content_info['content_type']}")
            if content_info['size']:
                size_mb = int(content_info['size']) / (1024 * 1024)
                print(f"📏 Size: {size_mb:.2f}MB")
            
            # Download the content
            content = response.content
            
            # Check for duplicates
            content_hash = self.calculate_hash(content)
            if content_hash in self.downloaded_hashes:
                print("⚠️ Duplicate image detected - skipping download")
                return False
            
            # Generate filename
            filename = self.generate_filename(url, content_info['content_type'])
            filepath = self.base_dir / filename
            
            # Handle filename conflicts
            counter = 1
            original_filepath = filepath
            while filepath.exists():
                name, ext = original_filepath.stem, original_filepath.suffix
                filepath = self.base_dir / f"{name}_{counter}{ext}"
                counter += 1
            
            # Save the image
            with open(filepath, 'wb') as f:
                f.write(content)
            
            # Record the hash
            self.downloaded_hashes.add(content_hash)
            
            print(f"✓ Successfully fetched: {filename}")
            print(f"✓ Image saved to: {filepath}")
            
            return True
            
        except requests.exceptions.Timeout:
            print("✗ Connection timeout - the community connection was slow")
        except requests.exceptions.ConnectionError:
            print("✗ Connection error - unable to reach the community resource")
        except requests.exceptions.HTTPError as e:
            print(f"✗ HTTP error: {e.response.status_code} - resource not accessible")
        except requests.exceptions.RequestException as e:
            print(f"✗ Request error: {e}")
        except IOError as e:
            print(f"✗ File save error: {e}")
        except Exception as e:
            print(f"✗ Unexpected error: {e}")
        
        return False
    
    def fetch_multiple_images(self, urls):
        """Handle multiple URLs - Ubuntu community spirit"""
        successful = 0
        total = len(urls)
        
        print(f"\n🤝 Processing {total} community resources...")
        
        for i, url in enumerate(urls, 1):
            print(f"\n--- Processing {i}/{total} ---")
            if self.fetch_single_image(url.strip()):
                successful += 1
        
        print(f"\n📊 Summary: {successful}/{total} images successfully downloaded")
        return successful
    
    def interactive_mode(self):
        """Interactive mode for single URL input"""
        print("Welcome to the Ubuntu Image Fetcher")
        print("A tool for mindfully collecting images from the web")
        print("Embodying the spirit: 'I am because we are'\n")
        
        if not self.create_directory():
            return
        
        while True:
            url = input("Please enter the image URL (or 'quit' to exit): ").strip()
            
            if url.lower() in ['quit', 'exit', 'q']:
                print("\n🙏 Thank you for sharing in the Ubuntu spirit!")
                break
            
            if not url:
                print("⚠️ Please provide a valid URL")
                continue
            
            success = self.fetch_single_image(url)
            
            if success:
                print("\n🌟 Connection strengthened. Community enriched.")
            
            # Ask if user wants to continue
            continue_choice = input("\nWould you like to fetch another image? (y/n): ").strip().lower()
            if continue_choice not in ['y', 'yes']:
                print("\n🙏 Thank you for sharing in the Ubuntu spirit!")
                break
    
    def batch_mode(self, urls):
        """Batch mode for multiple URLs"""
        print("Welcome to the Ubuntu Image Fetcher - Batch Mode")
        print("A tool for mindfully collecting images from the web")
        print("Embodying the spirit: 'I am because we are'\n")
        
        if not self.create_directory():
            return False
        
        successful = self.fetch_multiple_images(urls)
        
        if successful > 0:
            print("\n🌟 Connections strengthened. Community enriched.")
        
        return successful > 0

def main():
    """Main function with enhanced functionality and debug mode"""
    print("Ubuntu Image Fetcher")
    print("Choose your approach:")
    print("1. Interactive mode (single URLs)")
    print("2. Batch mode (multiple URLs)")
    print("3. Debug mode (with detailed logging)")
    
    choice = input("Enter your choice (1, 2, or 3): ").strip()
    
    debug_mode = choice == '3'
    if debug_mode:
        print("\n🐛 DEBUG MODE ENABLED - Detailed logging active")
        print("Choose your approach:")
        print("1. Interactive mode (single URLs)")
        print("2. Batch mode (multiple URLs)")
        choice = input("Enter your choice (1 or 2): ").strip()
    
    fetcher = UbuntuImageFetcher(debug=debug_mode)
    
    if choice == '2':
        print("\nBatch Mode: Enter URLs separated by commas or one per line")
        print("End with an empty line when done:")
        
        urls = []
        while True:
            try:
                line = input().strip()
                if not line:
                    break
                # Handle comma-separated URLs or single URL per line
                if ',' in line:
                    urls.extend([url.strip() for url in line.split(',') if url.strip()])
                else:
                    urls.append(line)
            except KeyboardInterrupt:
                print("\n\n⚠️ Interrupted by user")
                break
            except EOFError:
                break
        
        if urls:
            fetcher.batch_mode(urls)
        else:
            print("No URLs provided.")
    else:
        # Default to interactive mode
        fetcher.interactive_mode()

# Simple test function for debugging
def test_with_sample_urls():
    """Test function with some sample image URLs"""
    print("🧪 Testing with sample URLs...")
    
    sample_urls = [
        "https://httpbin.org/image/jpeg",  # Test JPEG
        "https://httpbin.org/image/png",   # Test PNG
        "https://httpbin.org/image/webp",  # Test WebP (might not work on all systems)
    ]
    
    fetcher = UbuntuImageFetcher(debug=True)
    
    if not fetcher.create_directory():
        print("❌ Cannot create directory for testing")
        return
    
    print(f"Testing with {len(sample_urls)} sample URLs...")
    success_count = fetcher.fetch_multiple_images(sample_urls)
    
    print(f"\n✅ Test completed: {success_count}/{len(sample_urls)} successful downloads")

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        print("Running in test mode. To run the main program, do not use the '--test' argument.")
        test_with_sample_urls()
    else:
        print("To run tests, use: python image_fetcher_script.py --test")
        main()