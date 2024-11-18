import sys
import os

# Add the parent directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from seven_deadly_swarms.seven_deadly_swarms import SevenDeadlySwarms

# Example usage
swarms = SevenDeadlySwarms()

content = "The product launch was a massive success with grand ambition and meticulous details."

# Add elements of the seven deadly sins
modified_content = swarms.add_elements(content)
print("Added Elements:", modified_content)

# Remove elements of the seven deadly sins
cleaned_content = swarms.remove_elements(content)
print("Removed Elements:", cleaned_content)
