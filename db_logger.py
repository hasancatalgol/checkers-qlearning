import psycopg2
from psycopg2.extras import execute_values

def connect_db():
    return psycopg2.connect(
        dbname="ql",
        user="admin",
        password="admin",
        host="localhost",
        port="5433"
    )

def log_metrics(metrics_list):
    conn = connect_db()
    cur = conn.cursor()
    insert_query = """
    INSERT INTO rl_metrics (
        episode, step, agent_name, action, reward, q_value, max_q, agent_pos, runner_pos
    ) VALUES %s
    """
    execute_values(cur, insert_query, metrics_list)
    conn.commit()
    cur.close()
    conn.close()
