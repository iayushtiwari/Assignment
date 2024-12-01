# Question One's Answer
Django Signals by defaultly are Synchronous, we can use sync_to_async() like function to work with synchronous function in asynchrounse context

# Question Two's Answer
Yes By defaultly Django signals runs on same thread as caller

# Question Three's Answer
Yes, by default, Django signals run in the same database transaction as the caller. This is because signals like post_save or post_delete are triggered after the corresponding database operation is executed, and they share the same transaction context unless explicitly handled otherwise