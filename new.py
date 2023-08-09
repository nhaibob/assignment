import os

# Define the block to search for
search_block = '''<header class="header">
    <div class="logo-container">
      <img src="pics\\ebook (1).png" alt="Apricity Logo" height="50" width="50">
    </div>
    <nav aria-label="Main Navigation" class="header-nav">
      <ul class="nav-list">
        <li class="nav-item"><a class="nav-link" href="index.html">Home</a></li>
        <li class="nav-item"><a class="nav-link" href="fictions.html">Fictions</a></li>
        <li class="nav-item"><a class="nav-link" href="nonfic.html">Non-fiction</a></li>
        <li class="nav-item"><a class="nav-link" href="children'sbooks.html">Children's Books</a></li>
        <li class="nav-item"><a class="nav-link" href="textbooks.html">Textbooks</a></li>
      </ul>
    </nav>
  </header>'''

# Define the block to replace it with
replace_block = '''  <header class="header">
    <div class="logo-container">
      <img src="pics/ebook (1).png" alt="Apricity Logo" height="50" width="50">
      
    </div>
    <input type="checkbox" id="click">
    <label for="click" class="hamburger">
      <i class="fa-solid fa-bars"></i>
    </label>
    <nav aria-label="Main Navigation" class="header-nav">
      <ul class="nav-list">
        <li class="nav-item"><a class="nav-link" href="index.html">Home</a></li>
        <li class="nav-item"><a class="nav-link" href="fictions.html">Fictions</a></li>
        <li class="nav-item"><a class="nav-link" href="nonfic.html">Non-fiction</a></li>
        <li class="nav-item"><a class="nav-link" href="children'sbooks.html">Children's Books</a></li>
        <li class="nav-item"><a class="nav-link" href="textbooks.html">Textbooks</a></li>
      </ul>
    </nav>
  </header>'''

# Loop over every file in the directory
for filename in os.listdir():
    if filename.endswith(".html"):
        with open(filename, 'r') as f:
            content = f.read()
        # If the search block is in the file, replace it
        if search_block in content:
            content = content.replace(search_block, replace_block)
            with open(filename, 'w') as f:
                f.write(content)
