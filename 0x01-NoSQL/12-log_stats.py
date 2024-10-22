#!/usr/bin/env python3
"""
Script to display statistics about Nginx logs stored in MongoDB.

Usage:
    ./100-stats_nginx <database_name>
"""

import sys
from pymongo import MongoClient


def main():
    if len(sys.argv) != 2:
        print("Usage: 100-stats_nginx <database_name>")
        sys.exit(1)
    
    db_name = sys.argv[1]

    try:
        # Connect to MongoDB (default host and port)
        client = MongoClient()
        db = client[db_name]
        collection = db.nginx

        # Total number of logs
        total_logs = collection.count_documents({})
        print(f"{total_logs} logs")

        # Methods statistics
        print("Methods:")
        methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
        for method in methods:
            count = collection.count_documents({'method': method})
            print(f"\t{method}: {count}")
        
        # Count of GET /status
        get_status = collection.count_documents({'method': 'GET', 'path': '/status'})
        print(f"GET /status: {get_status}")
    
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()

