# MySQL 5.7 Installation Guide

## Prerequisites

- SSH access to `web-01` and `web-02` servers.
- Ensure SSH project task #3 is completed.

## Installation Steps

### Step 1: Add MySQL APT Repository

1. Download the MySQL APT Repository package:

    ```bash
    wget https://dev.mysql.com/get/mysql-apt-config_0.8.22-1_all.deb
    ```

2. Install the repository package:

    ```bash
    sudo dpkg -i mysql-apt-config_0.8.22-1_all.deb
    ```

3. During installation, select MySQL 5.7 and proceed.

4. Update the package list:

    ```bash
    sudo apt update
    ```

5. Install MySQL server:

    ```bash
    sudo apt install mysql-server
    ```

6. Secure MySQL installation:

    ```bash
    sudo mysql_secure_installation
    ```

### Step 2: Verify MySQL Installation

Run the following command to verify the installation:

```bash
mysql --version
