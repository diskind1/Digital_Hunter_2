from db import db_connection
from logger import logger

# def conn_db():


def quality_goal_shift_alert():
    conn = db_connection()
    if not conn:
        logger.error("Connection to db failed")
        return None
    try:
        cursor = conn.cursor(dictionary=True)
        sql = """
        SELECT * 
        FROM targets
        WHERE priority_level = 1
        """
        cursor.execute(sql)
        res = cursor.fetchall()
        logger.info("Done")
        return res
    except Exception as e:
        logger.error("There was an error. {e}")
    finally:
        if conn:
            conn.close()


def analysis_of_collection_sources():
    conn = db_connection()
    if not conn:
        logger.error("Connection to db failed")
        return None
    try:
        cursor = conn.cursor(dictionary=True)
        sql = """
        SELECT signal_type, COUNT(*) as count_signal
        FROM intel_signals
        GROUP BY signal_type
        ORDER BY count_signal DESC
        """
        cursor.execute(sql)
        res = cursor.fetchall()
        logger.info("Done")
        return res
    except Exception as e:
        logger.error("There was an error. {e}")
    finally:
        if conn:
            conn.close()


def finding_new_targets():
    conn = db_connection()
    if not conn:
        logger.error("Connection to db failed")
        return None
    try:
        cursor = conn.cursor(dictionary=True)
        sql = """
        SELECT entity_id, COUNT(*) as count_reports
        FROM targets
        GROUP BY entity_id
        ORDER BY count_reports DESC
        LIMIT 3
        """
        cursor.execute(sql)
        res = cursor.fetchall()
        logger.info("Done")
        return res
    except Exception as e:
        logger.error("There was an error. {e}")
    finally:
        if conn:
            conn.close()


def identifying_awakened_sleeping_cells():
    conn = db_connection()
    if not conn:
        logger.error("Connection to db failed")
        return None
    try:
        cursor = conn.cursor(dictionary=True)
        sql = """

        """
        cursor.execute(sql)
        res = cursor.fetchall()
        logger.info("Done")
        return res
    except Exception as e:
        logger.error("There was an error. {e}")
    finally:
        if conn:
            conn.close()    



def visualization_of_a_target_trajectory():
    conn = db_connection()
    if not conn:
        logger.error("Connection to db failed")
        return None
    try:
        cursor = conn.cursor(dictionary=True)
        sql = """
        
        """
        cursor.execute(sql)
        res = cursor.fetchall()
        logger.info("Done")
        return res
    except Exception as e:
        logger.error("There was an error. {e}")
    finally:
        if conn:
            conn.close()    



def analyzing_escape_patterns_after_an_attack():
    conn = db_connection()
    if not conn:
        logger.error("Connection to db failed")
        return None
    try:
        cursor = conn.cursor(dictionary=True)
        sql = """
        
        """
        cursor.execute(sql)
        res = cursor.fetchall()
        logger.info("Done")
        return res
    except Exception as e:
        logger.error("There was an error. {e}")
    finally:
        if conn:
            conn.close()    


def meetings_between_targets_and_new_entities():
    conn = db_connection()
    if not conn:
        logger.error("Connection to db failed")
        return None
    try:
        cursor = conn.cursor(dictionary=True)
        sql = """
        
        """
        cursor.execute(sql)
        res = cursor.fetchall()
        logger.info("Done")
        return res
    except Exception as e:
        logger.error("There was an error. {e}")
    finally:
        if conn:
            conn.close()    