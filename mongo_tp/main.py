from data.insert_data import insert_initial_class
from operations.queries import find_students_with_high_final
from operations.updates import add_bob_and_update, add_charlie_and_remove_alice
from operations.aggregation import average_final, max_final
from utils.display import show_all_documents

if __name__ == "__main__":
    insert_initial_class()
    add_bob_and_update()
    find_students_with_high_final()
    add_charlie_and_remove_alice()
    average_final()
    max_final()
    show_all_documents()