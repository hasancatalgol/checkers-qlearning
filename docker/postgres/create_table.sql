CREATE TABLE rl_metrics (
    id SERIAL PRIMARY KEY,
    timestamp TIMESTAMPTZ DEFAULT NOW(),
    episode INT,
    step INT,
    agent_name TEXT,
    action TEXT,
    reward FLOAT,
    q_value FLOAT,
    max_q FLOAT,
    agent_pos TEXT,
    runner_pos TEXT
);