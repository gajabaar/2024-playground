# 2024-Playground Project

Welcome to the `2024-Playground` repository! This document will guide you through the setup process and understanding the contribution guidelines, which is essential for participating in this project.

## Steps for Contributing

* [Setting Up SSH Keys](./#setting-up-ssh-keys)
  * [Generating a New SSH Key](./#generating-a-new-ssh-key)
  * [Adding Your SSH Key to the ssh-agent](./#adding-your-ssh-key-to-the-ssh-agent)
  * [Adding the SSH Key to Your GitHub Account](./#adding-the-ssh-key-to-your-github-account)
* [Setting Up Your Own Copy of the Repository (Forked Repository)](./#setting-up-your-own-copy-of-the-repository)
* [Organizing Your Work](./#organizing-your-work)
* [Adding Changes](./#adding-changes)
* [Opening a Pull Request on GitHub](./#opening-a-pull-request-on-github)

### Setting Up SSH Keys

Setting up SSH keys allows you to securely connect to GitHub without needing to enter your username and password every time you interact with your repository from the command line.

#### **Generating a New SSH Key**

1.  Open a terminal and paste the following command with your email address:

    ```bash
    ssh-keygen -t rsa -b 4096 -C "sudogajendra@gmail.com"
    ```

    This creates a new SSH key, using the provided email as a label.
2.  When prompted to "Enter a file in which to save the key," press Enter. This accepts the default file location.

    ```bash
    > Enter file in which to save the key (/home/gajen/.ssh/id_rsa): [Press enter]
    ```

    That's it! Now your system has its own SSH keys ready to go.

<figure><img src=".files_for_readme/images/Generating a New SSH Key 0.png" alt=""><figcaption></figcaption></figure>

#### **Adding Your SSH Key to the ssh-agent**

1.  Start the ssh-agent in the background.

    ```bash
    eval "$(ssh-agent -s)"
    ```
2.  Add your SSH private key to the ssh-agent.

    ```bash
    ssh-add ~/.ssh/id_rsa
    ```

#### **Adding the SSH Key to Your GitHub Account**

1.  Copy the SSH key to your clipboard.

    ```bash
    sudo apt-get install xclip -y
    xclip -sel clip < ~/.ssh/id_rsa.pub
    ```

    Or, if `xclip` is not available:

    ```bash
    cat ~/.ssh/id_rsa.pub
    ```

    And then manually copy the output.
2.  In the upper-right corner of any page, click your **profile photo**,

    <figure><img src=".files_for_readme/images/Adding the SSH Key to Your GitHub Account 1.png" alt=""><figcaption></figcaption></figure>
3.  Then, click on **Settings**.

    <figure><img src=".files_for_readme/images/Adding the SSH Key to Your GitHub Account 2.png" alt=""><figcaption></figcaption></figure>
4.  In the user settings sidebar, click **SSH and GPG keys,** then click on "**New SSH key**"

    <figure><img src=".files_for_readme/images/Adding the SSH Key to Your GitHub Account 3.png" alt=""><figcaption></figcaption></figure>
5.  In the "Title" field, add a descriptive label for the new key. For example, if you're using a Linux on Virtual Machine, you might call this key "Linux on Virtual Machine". Then, Paste your public key into the "Key" field.

    <figure><img src=".files_for_readme/images/Adding the SSH Key to Your GitHub Account 4.png" alt=""><figcaption></figcaption></figure>

After inserting all the details, click 'Add SSH key' button. If it prompted for the password, confirm it by using your GitHub password. You will then receive a successful message, something like `You have successfully added the key 'Linux on Virtual Machine'`.

<figure><img src=".files_for_readme/images/Adding the SSH Key to Your GitHub Account 5.png" alt=""><figcaption></figcaption></figure>

### Setting Up Your Own Copy of the Repository

1.  **Fork the repo on GitHub to your personal account.** Click the `Fork` button on the `gajabaar/2024-playground` Public page. (This needs to be done only once.)

    <figure><img src=".files_for_readme/images/Setting Up Your Own Copy of the Repository 0.png" alt=""><figcaption></figcaption></figure>
2.  After clicking the **Fork button**, we will be redirected to a page where we can customize our forked repository. Here, we don't need to make any changes, as everything looks fine. So, we processed by clicking on `Create fork` button.

    <figure><img src=".files_for_readme/images/Setting Up Your Own Copy of the Repository 1.png" alt=""><figcaption></figcaption></figure>
3.  **Clone the repository:** Click on the green `Code` button. It will open a small window. Then click on `SSH` and copy the repository's URL using the copy button or by manually selecting the URL. This URL will be copied to your clipboard. You can use this URL to clone the repository onto your local machine.

    <figure><img src=".files_for_readme/images/Setting Up Your Own Copy of the Repository 2.png" alt=""><figcaption></figcaption></figure>

    Now, we have the SSH URL of our forked repository, we can use it to clone our forked repo onto our local machine using the command `git clone <repo URL>`.

    <figure><img src=".files_for_readme/images/Setting Up Your Own Copy of the Repository 3.png" alt=""><figcaption></figcaption></figure>

### Organizing your Work

When working on a specific challenge, ensure your contributions are organized as follows:

1. Create a directory similar to challenge name (e.g., `learning_Git` for learngitbranching, `cryptopals` for cryptopals ), etc., for their write-ups if directory is not present.
2. Within the challenge directory, create a subdirectory from your Name or username.
3. Place all your work for that challenge within your subdirectory.

Example structure:

```bash
/learning_Git/your_username/your_files_and_folders_here
# Example: 
# /learning_Git/GajendraMahato/1.1.introduction-sequence-write-up.md
# /learning_Git/GajendraMahato/1.2.ramping-up-write-up.md
```

### Adding Changes

1. **Navigate to Your Repository Directory**:
   *   Before making any changes, ensure you are in your local repository directory using the following command:

       ```bash
       cd 2024-playground
       ```
2. **List Existing Branches**:
   *   To view all existing branches in your local repository, use the command:

       ```bash
       git branch -a
       ```

       <figure><img src=".files_for_readme/images/Adding Changes 0.png" alt=""><figcaption></figcaption></figure>
3.  **Create and Switch to a New Branch**:

    * After cloning the repository, create a new branch for your changes and switch to it:

    ```bash
    git branch your_branch_name
    git checkout your_branch_name
    ```

    <figure><img src=".files_for_readme/images/Adding Changes 1.png" alt=""><figcaption></figcaption></figure>

    This step ensures that your changes are independent of the main branch until they are ready for integration, avoiding conflicts with other branches.
4. **Make Changes and Commit**:
   *   Once you have switched to your branch, make your desired changes to the codebase:

       ```bash
       git add .
       git commit -m "Descriptive message of what you did"
       ```

       <figure><img src=".files_for_readme/images/Adding Changes 2.png" alt=""><figcaption></figcaption></figure>
   * The `git add .` command stages all changes in your working directory for commit, while `git commit` records the changes with a descriptive message explaining the purpose of the commit.
5. **Push Your Changes**:
   *   Finally, push your committed changes to your forked repository on GitHub:

       ```bash
       git push origin your_branch_name
       ```

       <figure><img src=".files_for_readme/images/Adding Changes 3.png" alt=""><figcaption></figcaption></figure>
   * This command sends your local branch and commits to the remote repository, making them accessible for collaboration and review.

### Opening a Pull Request on GitHub

1. **Switch to Your Branch on GitHub**:
   *   Navigate to your forked repository on GitHub. Make sure you switch to the branch where you made your changes.

       <figure><img src=".files_for_readme/images/Opening a Pull Request on GitHub 0.png" alt=""><figcaption></figcaption></figure>
2. **Initiate a Pull Request**:
   *   Click on the green `Compare & pull request` button. If this button is not available, click on the `Contribute` button, then select `Open a pull request`.

       <figure><img src=".files_for_readme/images/Opening a Pull Request on GitHub 1.png" alt=""><figcaption></figcaption></figure>
3. **Describe Your Changes**:
   * You will be taken to a new page where you can describe the changes you made. Provide a clear and concise description of your changes in the provided text box. This helps the repository maintainers understand the purpose and context of your modifications.
4. **Open the Pull Request**:
   *   After describing your changes, click on the `Create pull request` button to open your pull request.

       <figure><img src=".files_for_readme/images/Opening a Pull Request on GitHub 2.png" alt=""><figcaption></figcaption></figure>
5. **Review and Feedback**:
   * Once your pull request is open, the repository's maintainers will review it. They will check the changes and decide whether to merge them into the main branch. If they find any issues or have suggestions, they will provide feedback. Be ready to make additional changes if requested.

By following these steps, you can contribute to the `2024-Playground` repository and collaborate effectively with other contributors. Happy learning!
