"""
=======================================================================
Hostel Management System - Resident Class & Search/Display Functions
=======================================================================
Main Components:
1. Resident class to store student information
2. Search function to find residents by room number
3. Display functions to view all residents and waiting list
=======================================================================
"""


class Resident:
    """
    Resident class to store hostel resident information

    Attributes:
        name (str): Student's full name
        student_id (str): Unique student ID number
        contact (str): Phone number or email
    """

    def __init__(self, name, student_id, contact):
        """
        Initialize a new Resident object

        Args:
            name (str): Student's name
            student_id (str): Student ID
            contact (str): Contact information
        """
        self.name = name
        self.student_id = student_id
        self.contact = contact

    def to_dict(self):
        """
        Convert Resident object to dictionary for JSON serialization

        Returns:
            dict: Dictionary containing resident data
        """
        return {
            'name': self.name,
            'student_id': self.student_id,
            'contact': self.contact
        }

    def __str__(self):
        """
        String representation of Resident for display

        Returns:
            str: Formatted string of resident details
        """
        return f"Name: {self.name} | ID: {self.student_id} | Contact: {self.contact}"


class HostelManager:
    """
    Main Hostel Management System class
    Contains Dictionary for rooms and Queue for waiting list
    """

    def __init__(self, total_rooms=10):
        """
        Initialize the Hostel Manager

        Args:
            total_rooms (int): Maximum number of rooms in the hostel
        """
        self.rooms = {}  # Dictionary: {room_number: Resident object}
        self.waiting_list = []  # Queue (using list): [Resident objects]
        self.total_rooms = total_rooms

    # ========== CORE SEARCH & DISPLAY FUNCTIONS ==========

    def search_resident(self, room_number):
        """
        Search for a resident by room number
        Time Complexity: O(1) - Dictionary lookup

        Args:
            room_number (str): Room number to search

        Returns:
            Resident or None: Resident object if found, None otherwise
        """
        # Check if room number exists in dictionary
        if room_number in self.rooms:
            resident = self.rooms[room_number]
            print(f"\n✓ Resident found in Room {room_number}:")
            print(f"  {resident}")
            return resident
        else:
            print(f"\n✗ No resident found in Room {room_number}")
            return None

    def display_all(self):
        """
        Display all current residents (Traverse operation)
        Time Complexity: O(n) - Iterate through all rooms
        """
        print("\n" + "=" * 60)
        print("CURRENT HOSTEL RESIDENTS".center(60))
        print("=" * 60)

        if not self.rooms:
            print("No residents currently checked in.")
        else:
            print(f"Total Occupied Rooms: {len(self.rooms)}/{self.total_rooms}\n")

            # Sort rooms by room number for better display
            sorted_rooms = sorted(self.rooms.items())

            for room_number, resident in sorted_rooms:
                print(f"Room {room_number}: {resident}")

        print("=" * 60)

        # Also display waiting list if any
        self.display_waiting_list()

    def display_waiting_list(self):
        """
        Display all students in the waiting list
        """
        print("\n" + "-" * 60)
        print("WAITING LIST (Queue - FIFO)".center(60))
        print("-" * 60)

        if not self.waiting_list:
            print("Waiting list is empty.")
        else:
            print(f"Total in Queue: {len(self.waiting_list)}\n")

            for i, resident in enumerate(self.waiting_list, 1):
                print(f"Position {i}: {resident}")

        print("-" * 60)

    # ========== SUPPORTING HELPER FUNCTIONS ==========

    def is_room_available(self, room_number):
        """
        Check if a specific room is available

        Args:
            room_number (str): Room number to check

        Returns:
            bool: True if available, False if occupied
        """
        return room_number not in self.rooms

    def get_occupancy_rate(self):
        """
        Calculate current occupancy percentage

        Returns:
            float: Occupancy rate as percentage
        """
        return (len(self.rooms) / self.total_rooms) * 100


# ========== DEMONSTRATION / TESTING CODE ==========

def demo_functions():
    """
    Demonstration of Resident Class and Search/Display Functions
    """
    print("\n" + "=" * 60)
    print("DEMO: RESIDENT CLASS & SEARCH/DISPLAY FUNCTIONS")
    print("=" * 60)

    # Initialize hostel manager
    hostel = HostelManager(total_rooms=5)

    # Create some sample residents
    print("\n[Creating sample residents...]")
    resident1 = Resident("Ahmad Zaki", "A001", "012-3456789")
    resident2 = Resident("Siti Nur", "A002", "013-9876543")
    resident3 = Resident("Kumar Raj", "A003", "014-5551234")

    # Manually add to rooms (simulating check-in)
    hostel.rooms["101"] = resident1
    hostel.rooms["102"] = resident2
    hostel.rooms["105"] = resident3

    # Add to waiting list (simulating full hostel scenario)
    waiting1 = Resident("Lee Ming", "A004", "015-7778888")
    waiting2 = Resident("Fatimah Ali", "A005", "016-3332222")
    hostel.waiting_list.append(waiting1)
    hostel.waiting_list.append(waiting2)

    print("✓ Sample data created successfully!\n")

    # Test 1: Display all residents
    input("Press ENTER to display all residents...")
    hostel.display_all()

    # Test 2: Search for existing resident
    input("\nPress ENTER to search for Room 102...")
    hostel.search_resident("102")

    # Test 3: Search for non-existing resident
    input("\nPress ENTER to search for Room 104 (empty)...")
    hostel.search_resident("104")

    # Test 4: Check occupancy
    print(f"\nCurrent Occupancy Rate: {hostel.get_occupancy_rate():.1f}%")

    print("\n" + "=" * 60)
    print("DEMO COMPLETED - All functions working correctly!")
    print("=" * 60)


# Run demonstration
if __name__ == "__main__":
    demo_functions()