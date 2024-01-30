# Caching
* Caching System:
> * A caching system is a mechanism used to store and manage copies of frequently accessed or computationally expensive data in a faster and more easily retrievable location. The purpose of caching is to improve data access times and overall system performance by reducing the need to fetch the same data repeatedly from the original source.

* FIFO (First-In-First-Out):
> * FIFO is a caching algorithm where the oldest item that was added to the cache is the first one to be removed when the cache reaches its limit. It follows the principle of a queue, where the items are added to the back and removed from the front.

* LIFO (Last-In-First-Out):
> * LIFO is a caching algorithm where the most recently added item is the first to be removed when the cache reaches its limit. It follows the principle of a stack, where items are added and removed from the same end.

* LRU (Least Recently Used):
> * LRU is a caching algorithm that removes the least recently used items first when the cache is full. It keeps track of the order in which items are accessed and prioritizes retaining the most recently used items.

* MRU (Most Recently Used):
> * MRU is a caching algorithm that removes the most recently used items first when the cache is full. It prioritizes retaining items that have been accessed most recently.

* LFU (Least Frequently Used):
> * LFU is a caching algorithm that removes the least frequently used items first when the cache is full. It keeps track of how often each item is accessed and prioritizes retaining items that are accessed less frequently.

* Purpose of a Caching System:
> * The primary purpose of a caching system is to improve the efficiency and performance of a system by reducing the time and resources required to access frequently used data. Caching helps to minimize latency and response times, particularly in scenarios where fetching data from the original source is time-consuming or resource-intensive.

* Limits of a Caching System:
> * Size Limitations: Caches have finite sizes, and if the cache becomes full, a decision must be made on which items to remove.
> * Consistency Challenges: Caches may become inconsistent with the original data source if the data is updated outside the cache.
> * Invalidation Issues: Ensuring that cached data is still valid and up-to-date can be challenging, especially in dynamic environments.
> * Complexity: Implementing and managing caching mechanisms adds complexity to a system, requiring careful consideration of cache eviction policies and synchronization.
