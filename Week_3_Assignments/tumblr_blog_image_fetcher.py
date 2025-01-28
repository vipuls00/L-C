import requests
import json
import time

class Blog:
    def __init__(self, blog_name):
        self.blog_name = blog_name
        self.title = None
        self.name = None
        self.description = None
        self.no_of_posts = None

    def fetch_info(self):
        url = f"https://{self.blog_name}.tumblr.com/api/read/json"
        response = self._make_request(url, params={'num': 1})  # Fetching only a single post at once to get blog info.
        if response:
            data = self._parse_response(response.text)
            if data:
                self._extract_blog_info(data)

    def _make_request(self, url, params):
        for attempt in range(5):
            try:
                response = requests.get(url, params=params)
                response.raise_for_status()  # Raises an HTTPError for bad responses (4xx and 5xx)
                return response  
            except requests.exceptions.RequestException as e:
                if attempt == 4:  
                    raise
                else:
                    continue  

    def _parse_response(self, response_text):
        if response_text.strip():
            try:
                json_data = response_text[response_text.find('{'):-2]  # Removing the key tumblelog to get only required json data 
                return json.loads(json_data)
            except ValueError as e:
                print(f"Error decoding JSON: {e}")
        else:
            print("Empty response received from the server.")
        return None

    def _extract_blog_info(self, data):
        blog_info = data.get('tumblelog', {})
        self.title = blog_info.get('title', 'No Title')
        self.name = blog_info.get('name', 'No Name')
        self.description = blog_info.get('description', 'No Description')
        self.no_of_posts = data.get('posts-total', 0)

    def display_info(self):
        print(f"title: {self.title}")
        print(f"name: {self.name}")
        print(f"description: {self.description}")
        print(f"no of posts: {self.no_of_posts}")


class ImageFetcher:
    def __init__(self, blog_name):
        self.blog_name = blog_name

    def build_image_url(self, photo, resolution='1280'):  # Only fetching the highest resolution image
        if f'photo-url-{resolution}' in photo:
            key = f"photo-url-{resolution}"
        return photo.get(key)

    def fetch_images_from_post(self, post, post_number):
        images = []
        if 'photos' in post:
            for photo in post['photos']:
                image_url = self.build_image_url(photo)
                if image_url:
                    images.append((post_number, image_url))
        return images

    def fetch_images_from_range(self, starting_range, ending_range):
        images = []
        for post_number in range(starting_range, ending_range + 1):
            start_index = post_number - 1
            url = f"https://{self.blog_name}.tumblr.com/api/read/json"
            response = self._make_request(url, params={'num': 1, 'start': start_index})
            print(f"Fetching post {post_number}")

            if response:
                data = self._parse_response(response.text)
                if data:
                    posts = data.get('posts', [])
                    if not posts:
                        print(f"No posts found at post number {post_number}.")
                    for post in posts:
                        images_from_post = self.fetch_images_from_post(post, post_number)
                        if images_from_post:
                            images.extend(images_from_post)
                        else:
                            print(f"No images found in post {post_number}.")
        return images

    def _make_request(self, url, params):
        for attempt in range(5):
            try:
                response = requests.get(url, params=params)
                response.raise_for_status()
                return response
            except requests.exceptions.HTTPError as e:
                if response.status_code == 429:
                    retry_after = int(response.headers.get("Retry-After", 1))
                    print(f"Rate limit reached. Retrying after {retry_after} seconds...")
                    time.sleep(retry_after)
                else:
                    print(f"HTTPError: {e}")
                    break
            except requests.exceptions.RequestException as e:
                print(f"Request failed: {e}")
                break
        return None

    def _parse_response(self, response_text):
        if response_text.strip():
            try:
                json_data = response_text[response_text.find('{'):-2]
                return json.loads(json_data)
            except ValueError as e:
                print(f"Error decoding JSON: {e}")
        else:
            print("Empty response received from the server.")
        return None


class TumblrAPIClient:
    def __init__(self, blog_name):
        self.blog = Blog(blog_name)
        self.image_fetcher = ImageFetcher(blog_name)

    def fetch_and_display_blog_info(self):
        self.blog.fetch_info()
        self.blog.display_info()

    def fetch_and_display_images(self, start, end):
        images = self.image_fetcher.fetch_images_from_range(start, end)
        self.display_images(images)

    def display_images(self, images):
        if images:
            for post_no, img_url in images:
                print(f"{post_no}. {img_url}")
        else:
            print("No images found in the specified range.")

    def validate_range(self, post_range):
        try:
            starting_range, ending_range = map(int, post_range.split('-'))
            if starting_range < 1 or ending_range < starting_range:
                raise ValueError("Invalid range values")
            return starting_range, ending_range
        except ValueError as e:
            print(f"Error in range input: {e}")
            return None, None


def main():
    blog_name = input("Enter the Tumblr blog name: ").strip()
    post_range = input("Enter the range (start-end): ").strip()

    client = TumblrAPIClient(blog_name)

    start, end = client.validate_range(post_range)
    if start is None or end is None:
        return

    client.fetch_and_display_blog_info()
    client.fetch_and_display_images(start, end)


if __name__ == "__main__":
    main()
