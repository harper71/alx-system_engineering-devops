To show the SSH keys on a Linux system, you typically need to check the contents of the SSH key files stored in your home directory. Here’s how you can do it:

Displaying Existing SSH Keys
Open a Terminal: Access your terminal or SSH into your Linux machine.

Navigate to the SSH Directory: SSH keys are usually stored in the ~/.ssh directory. You can navigate to this directory by running:

bash
Copy code
cd ~/.ssh
List the Files: List the files in the directory to see your SSH keys. The private key files usually end in .pem or do not have an extension, while the public key files end in .pub. Common names for SSH key pairs are id_rsa (private key) and id_rsa.pub (public key).

bash
Copy code
ls -l
View the Public Key: To display the content of a public key file, use the cat command. For example, to show the content of the id_rsa.pub file, run:

bash
Copy code
cat id_rsa.pub
The output will look something like this:

plaintext
Copy code
ssh-rsa AAAAB3... rest of your key ... username@hostname
Generating SSH Keys (If None Exist)
If you don't have an SSH key pair and need to generate one, you can use the ssh-keygen command:

Generate a New SSH Key Pair:

bash
Copy code
ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
This command generates a new SSH key pair using the RSA algorithm with a 4096-bit key size. The -C flag adds a comment to the key, typically your email address.

Follow the Prompts:

Enter file in which to save the key: Press Enter to accept the default file location (/home/your_username/.ssh/id_rsa).
Enter passphrase (empty for no passphrase): Optionally, enter a passphrase for added security or press Enter for no passphrase.
Enter same passphrase again: Confirm the passphrase.
View the New SSH Keys: After generating the keys, you can view them as described in the previous section by navigating to the ~/.ssh directory and using the cat command to display the contents of the .pub file.

Summary
To display existing keys:

bash
Copy code
cd ~/.ssh
ls -l
cat id_rsa.pub
To generate new keys:

bash
Copy code
ssh-keygen -t rsa -b 4096 -C "your_email@example.com"