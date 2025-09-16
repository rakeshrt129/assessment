
from fastapi.responses import StreamingResponse
import csv
from io import StringIO

def export_results_csv(results):
    output = StringIO()
    writer = csv.DictWriter(output, fieldnames=results[0].keys())
    writer.writeheader()
    writer.writerows(results)
    output.seek(0)
    return StreamingResponse(output, media_type="text/csv", headers={"Content-Disposition": "attachment; filename=results.csv"})
