# Architectural Patterns

### **1. Layered Architecture**

Code is arranged in layers, with data passing through them. This pattern simplifies maintenance and allows for easy scalability of web and cloud applications.

### **2. Client-Server**

Involves a set of clients and a server, where clients send requests to the server for processing. It enables centralized data access and supports cross-platform development.

### **3. Master-Slave**

Clients make multiple instances of the same request, and the master distributes the workload to slave nodes for parallel processing. It is suitable for multi-threaded applications but lacks automated failover.

### **4. Pipe-Filter** 

Complex processing is divided into separate tasks or filters that process data through pipes. It enables code reusability and parallel processing, but data loss can occur between filters.

### **5. Broker**

Components in a distributed system provide independent services, and a central broker coordinates requests and responses between clients and servers. It simplifies development in a distributed environment.

### **6. Peer-to-Peer (P2P)**

Each computer in the network has equal authority, and they can function as both clients and servers. P2P networks are decentralized and offer increased security, but performance limitations can arise under heavy load.

### **7. Event-Bus**

Components act only when there is relevant data to be processed, and a central event bus routes the data to the appropriate modules. It handles complexity, scalability, and extensibility but requires careful testing and has messaging overhead.

### **8. Model-View-Controller (MVC)**

Separates the data model, presentation layer, and control aspects of an application. It expedites development, supports multiple views, and enables UI changes without modifying the underlying model.

### **9. Blackboard**

Used in emerging domains like AI and ML, it involves a blackboard for storing information, knowledge resources for updating the blackboard, and a controller for updating application assets. It facilitates experiments but lacks a settled architecture pattern.

### **10. Interpreter**

Deals with the grammar of programming languages and provides an interpreter for the language. It uses expressions and a tree structure to evaluate the language's syntax. It is commonly used in creating classes from symbols in programming languages.
