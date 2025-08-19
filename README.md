# 🚆 Virtual Train Route Planner

## 📌 Overview

The Virtual Train Route Planner simulates a train network where passengers can navigate between stations in real time.
It uses doubly linked lists for forward/backward navigation of stations, and circular linked lists for loop routes (e.g., metro circles).


---

## ✅ Advantages

- Forward & Backward Navigation: Users can move along the route just like in real train travel.

- Circular Routes Supported: Perfect for metro loops (e.g., ring lines in cities).

- Efficient Representation: Linked lists dynamically manage stations without fixed size.

- Educational: Demonstrates doubly linked list and circular linked list in a real-world application.



---

## 🗂️ Data Structures Used

->  Doubly Linked List → For forward/backward navigation along linear routes.

-> Circular Linked List → For loop routes (e.g., city circular/metro).

-> List/Array → For maintaining all train lines in the system.



---

## 🎯 Usefulness

- Models real-world metro/train systems for navigation.

- Shows how linked lists help in dynamic route planning.

- Can be extended into a full path-finding system (with algorithms like Dijkstra).

- Good for DSA practice projects and transportation simulations.



---

## 🛠️ Why We Use This Project

Train and metro systems need efficient route planning.
This project demonstrates how linked lists can model stations, allowing navigation without needing arrays or indexes.


---

## 🔹 Sample Output

### ===== Linear Route Example =====
#### ➡️ Forward Navigation:
###### 🚉 Station A
###### 🚉 Station B
###### 🚉 Station C
###### 🚉 Station D
#### ⬅️ Backward Navigation:
###### 🚉 Station D
###### 🚉 Station C
###### 🚉 Station B
###### 🚉 Station A

### ===== Circular Route Example =====
#### ➡️ Forward Navigation:
###### 🚉 Metro 1
###### 🚉 Metro 2
###### 🚉 Metro 3
###### 🚉 Metro 4
###### 🚉 Metro 1
###### 🚉 Metro 2
#### ⬅️ Backward Navigation:
###### 🚉 Metro 4
###### 🚉 Metro 3
###### 🚉 Metro 2
###### 🚉 Metro 1
###### 🚉 Metro 4
###### 🚉 Metro 3

---
