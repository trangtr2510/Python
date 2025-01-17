from collections import deque
from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup

class WebPathFinder:
    def __init__(self):
        self.visited = set()
        
# Hàm lấy tất cả các liên kết từ một trang web
    def get_links(self, url):
        try:
            response = requests.get(url, timeout=5)
            soup = BeautifulSoup(response.text, 'html.parser')
            links = set()
            
            for link in soup.find_all('a'):
                href = link.get('href')
                if href:
                    absolute_url = urljoin(url, href)
                    links.add(absolute_url)
                    
            return links
        except Exception as e:
            print(f"Lỗi khi truy cập {url}: {str(e)}")
            return set()

# Hàm tìm đường đi ngắn nhất dùng BFS - tìm kiếm theo chiều rộng 
    def bfs_search(self, start_url, target_url, max_depth=10):
        if start_url == target_url:
            return [start_url]
            
        queue = deque([(start_url, [start_url])])
        self.visited = {start_url}
        depth = 0
        
        # Dictionary để lưu trữ parent của mỗi URL để truy vết đường đi
        parent = {start_url: None}
        
        while queue and depth < max_depth:
            level_size = len(queue)
            depth += 1
            
            # Xử lý từng level của BFS
            for _ in range(level_size):
                current_url, path = queue.popleft()
                
                # Lấy tất cả các liên kết từ trang hiện tại
                for next_url in self.get_links(current_url):
                    if next_url == target_url:
                        # Đã tìm thấy đường đi
                        return path + [next_url]
                        
                    if next_url not in self.visited:
                        self.visited.add(next_url)
                        queue.append((next_url, path + [next_url]))
                        parent[next_url] = current_url
        
        return None
# Hàm tìm đường đi sử dụng tìm kiếm hai chiều 
    def bidirectional_search(self, start_url, target_url, max_depth=5):
        if start_url == target_url:
            return [start_url]
            
        # Queue và visited set cho cả hai hướng
        forward_queue = deque([start_url])
        backward_queue = deque([target_url])
        
        forward_visited = {start_url: [start_url]}
        backward_visited = {target_url: [target_url]}
        
        depth = 0
        while forward_queue and backward_queue and depth < max_depth:
            depth += 1
            
            # Mở rộng từ phía start_url
            level_size = len(forward_queue)
            for _ in range(level_size):
                current_url = forward_queue.popleft()
                
                for next_url in self.get_links(current_url):
                    if next_url in backward_visited:
                        # Tìm thấy điểm giao
                        forward_path = forward_visited[current_url] + [next_url]
                        backward_path = backward_visited[next_url]
                        # Kết hợp hai đường đi
                        return forward_path[:-1] + backward_path[::-1]
                        
                    if next_url not in forward_visited:
                        forward_queue.append(next_url)
                        forward_visited[next_url] = forward_visited[current_url] + [next_url]
            
            # Mở rộng từ phía target_url
            level_size = len(backward_queue)
            for _ in range(level_size):
                current_url = backward_queue.popleft()
                
                for next_url in self.get_links(current_url):
                    if next_url in forward_visited:
                        # Tìm thấy điểm giao
                        forward_path = forward_visited[next_url]
                        backward_path = backward_visited[current_url] + [next_url]
                        # Kết hợp hai đường đi
                        return forward_path[:-1] + backward_path[::-1]
                        
                    if next_url not in backward_visited:
                        backward_queue.append(next_url)
                        backward_visited[next_url] = backward_visited[current_url] + [next_url]
        
        return None

def main():
    finder = WebPathFinder()
    
    # Ví dụ sử dụng
    start_url = "https://vnexpress.net/"
    target_url = "https://vnexpress.net/thu-tuong-xay-nha-may-dien-hat-nhan-ninh-thuan-trong-5-nam-4839509.html"
    
    print("Tìm kiếm sử dụng BFS:")
    path = finder.bfs_search(start_url, target_url)
    if path:
        print("Tìm thấy đường đi:")
        for i, url in enumerate(path):
            print(f"{i+1}. {url}")
    else:
        print("Không tìm thấy đường đi")
        
    print("\nTìm kiếm hai chiều:")
    path = finder.bidirectional_search(start_url, target_url)
    if path:
        print("Tìm thấy đường đi:")
        for i, url in enumerate(path):
            print(f"{i+1}. {url}")
    else:
        print("Không tìm thấy đường đi")

if __name__ == "__main__":
    main()