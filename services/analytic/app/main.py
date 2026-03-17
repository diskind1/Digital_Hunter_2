from fastapi import FastAPI
import uvicorn
from queries import quality_goal_shift_alert, analysis_of_collection_sources, finding_new_targets, identifying_awakened_sleeping_cells, visualization_of_a_target_trajectory, analyzing_escape_patterns_after_an_attack, meetings_between_targets_and_new_entities


app = FastAPI()

@app.get("/quality_goal_shift_alert")
def quality_goal_shift_alert_api():
    return quality_goal_shift_alert()

@app.get("/analysis_of_collection_sources")
def analysis_of_collection_sources_api():
    return analysis_of_collection_sources()

@app.get("/finding_new_targets")
def finding_new_targets_api():
    return finding_new_targets()

@app.get("/identifying_awakened_sleeping_cells")
def identifying_awakened_sleeping_cells_api():
    return identifying_awakened_sleeping_cells()

@app.get("/visualization_of_a_target_trajectory")
def visualization_of_a_target_trajectory_api():
    return visualization_of_a_target_trajectory()

@app.get("/analyzing_escape_patterns_after_an_attack")
def analyzing_escape_patterns_after_an_attack_api():
    return analyzing_escape_patterns_after_an_attack()

@app.get("/meetings_between_targets_and_new_entities")
def meetings_between_targets_and_new_entities_api():
    return meetings_between_targets_and_new_entities()

if __name__=="__main__":
    uvicorn.run(app, host="0.0.0.0, port=8000")