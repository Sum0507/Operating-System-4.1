from collections import deque

def fifo_page_replacement(pages, frame_size):
    frames = set()          # to quickly check presence
    queue = deque()         # to maintain FIFO order
    
    hit = 0
    miss = 0

    for page in pages:
        if page in frames:
            hit += 1
            print(f"Page {page}: HIT -> {list(queue)}")
        else:
            miss += 1
            
            if len(frames) < frame_size:
                frames.add(page)
                queue.append(page)
            else:
                old_page = queue.popleft()
                frames.remove(old_page)
                
                frames.add(page)
                queue.append(page)

            print(f"Page {page}: MISS -> {list(queue)}")

    print("\nFinal Result:")
    print("Hit count =", hit)
    print("Miss count =", miss)


# Example
pages = [7, 0, 1, 2, 0, 3, 0, 4]
frame_size = 3

fifo_page_replacement(pages, frame_size)