class Solution:
    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        MOD = 10**9 + 7

        # 1. Create events and collect all unique y-coordinates.
        events = []  # Each event is a tuple (x, y1, y2, type)
        y_coords = set()
        for x1, y1, x2, y2 in rectangles:
            # When we enter a rectangle at x1, add the y-interval.
            events.append((x1, y1, y2, 1))
            # When we leave a rectangle at x2, remove the y-interval.
            events.append((x2, y1, y2, -1))
            y_coords.add(y1)
            y_coords.add(y2)
        
        # Sort events by x-coordinate.
        events.sort()
        
        # 2. Discretize the y-coordinates.
        ys = sorted(y_coords)
        y_to_index = {v: i for i, v in enumerate(ys)}
        n = len(ys)
        
        # 3. Build a segment tree.
        # The segment tree array will cover indices [0, n-1].
        # We need two arrays:
        #  - cover: count of how many times an interval has been added.
        #  - segtree: total covered length in that segment.
        cover = [0] * (4 * n)
        segtree = [0] * (4 * n)
        
        def update(idx, left, right, ql, qr, val):
            """
            Recursively update the segment tree.
            
            idx: current index in the segment tree arrays.
            [left, right): current segment covered by this node.
            [ql, qr): query interval (the y-interval we want to update).
            val: the value to add (1 for an add event, -1 for a remove event).
            """
            # If current segment is completely outside the update interval, do nothing.
            if ql >= right or qr <= left:
                return
            
            # If current segment is fully within the update interval.
            if ql <= left and right <= qr:
                cover[idx] += val
            else:
                mid = (left + right) // 2
                update(idx * 2, left, mid, ql, qr, val)
                update(idx * 2 + 1, mid, right, ql, qr, val)
            
            # Update the current node's segtree value.
            # If this segment is covered by at least one rectangle, then the full segment length is covered.
            if cover[idx] > 0:
                segtree[idx] = ys[right] - ys[left]
            else:
                # If we are at a leaf node, then no length is covered.
                if right - left == 1:
                    segtree[idx] = 0
                else:
                    segtree[idx] = segtree[idx * 2] + segtree[idx * 2 + 1]
        
        # 4. Process events with the sweep-line.
        prev_x = events[0][0]
        area = 0
        
        for x, y1, y2, typ in events:
            # Compute the horizontal distance (dx) between current x and the previous x.
            dx = x - prev_x
            # Multiply dx by the total y-length covered at the previous x position.
            area = (area + dx * segtree[1]) % MOD
            
            # Update the segment tree with the current event.
            # Convert the actual y-values to their corresponding indices.
            update(1, 0, n - 1, y_to_index[y1], y_to_index[y2], typ)
            prev_x = x

        return area
