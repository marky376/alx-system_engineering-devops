### Web Server:

- **Role**: Stores, processes, and delivers web content to users upon request.
- **Analogy**: Like a chef preparing and serving food.
- **Functionality**: Handles incoming requests, retrieves requested resources, and sends them back to clients.
- **Examples**: Apache, Nginx, Microsoft IIS.

### Child Process:

- **Definition**: A process created by another process, known as the parent process.
- **Analogy**: A helper doing tasks for the main person.
- **Functionality**: Operates independently but shares certain attributes with its parent.
- **Purpose**: Used for multitasking and executing tasks concurrently.

### Parent and Child Processes in Web Servers:

- **Model**: Web servers often use a parent-child process model.
- **Parent Process**: Initiates the server and manages child processes.
- **Child Processes**: Handle incoming requests independently.
- **Purpose**: Improves server responsiveness and scalability.

### Main HTTP Requests:

1. **GET**: Requests a representation of a resource.
2. **POST**: Submits data to be processed to a specified resource.
3. **PUT**: Updates a resource or creates a new one if it doesn't exist.
4. **DELETE**: Deletes the specified resource.
5. **HEAD**: Requests headers that would be returned if a GET request were made.
6. **OPTIONS**: Requests information about the communication options available for the target resource.
7. **PATCH**: Applies partial modifications to a resource.

### DNS (Domain Name System):

- **Definition**: Decentralized naming system translating domain names into IP addresses.
- **Analogy**: Like a phone book for the internet.
- **Role**: Enables users to access resources using human-readable domain names.
- **Functionality**: Translates domain names into IP addresses and vice versa.

### DNS Record Types:

1. **A (Address) Record**: Maps a domain name to an IPv4 address.
2. **CNAME (Canonical Name) Record**: Alias of one domain name to another canonical domain name.
3. **TXT (Text) Record**: Contains arbitrary text information associated with a domain.
4. **MX (Mail Exchange) Record**: Specifies mail servers responsible for receiving email messages for a domain.

