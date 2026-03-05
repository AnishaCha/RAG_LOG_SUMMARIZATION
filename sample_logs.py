DUMMY_LOG = """
[2025-11-01 10:01:12] ERROR order-db: ORA-12541: TNS:no listener
[2025-11-01 10:01:15] WARN order-api: Connection timeout to order-db
[2025-11-01 10:01:16] INFO k8s: Pod order-db restarted
[2025-11-01 10:02:00] INFO deploy: deployment started
[2025-11-01 10:02:05] ERROR network: ACL update failed
[2025-11-01 10:03:33] ERROR order-db: ORA-01033 initialization in progress
[2025-11-01 10:05:00] INFO monitoring: latency spike
[2025-11-01 10:07:44] INFO deploy: deployment completed
"""