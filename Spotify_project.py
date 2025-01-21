import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsgluedq.transforms import EvaluateDataQuality

args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Default ruleset used by all target nodes with data quality enabled
DEFAULT_DATA_QUALITY_RULESET = """
    Rules = [
        ColumnCount > 0
    ]
"""

# Script generated for node album
album_node1737494565351 = glueContext.create_dynamic_frame.from_options(format_options={"quoteChar": "\"", "withHeader": True, "separator": ",", "optimizePerformance": False}, connection_type="s3", format="csv", connection_options={"paths": ["s3://project-spotify-etl-bucket/staging/albums.csv"], "recurse": True}, transformation_ctx="album_node1737494565351")

# Script generated for node track
track_node1737494566517 = glueContext.create_dynamic_frame.from_options(format_options={"quoteChar": "\"", "withHeader": True, "separator": ",", "optimizePerformance": False}, connection_type="s3", format="csv", connection_options={"paths": ["s3://project-spotify-etl-bucket/staging/track.csv"], "recurse": True}, transformation_ctx="track_node1737494566517")

# Script generated for node artist
artist_node1737494566027 = glueContext.create_dynamic_frame.from_options(format_options={"quoteChar": "\"", "withHeader": True, "separator": ",", "optimizePerformance": False}, connection_type="s3", format="csv", connection_options={"paths": ["s3://project-spotify-etl-bucket/staging/artists.csv"], "recurse": True}, transformation_ctx="artist_node1737494566027")

# Script generated for node Join album & artist
Joinalbumartist_node1737494631170 = Join.apply(frame1=album_node1737494565351, frame2=artist_node1737494566027, keys1=["artist_id"], keys2=["id"], transformation_ctx="Joinalbumartist_node1737494631170")

# Script generated for node Join with tracks
Joinwithtracks_node1737494696299 = Join.apply(frame1=Joinalbumartist_node1737494631170, frame2=track_node1737494566517, keys1=["track_id"], keys2=["track_id"], transformation_ctx="Joinwithtracks_node1737494696299")

# Script generated for node Drop Fields
DropFields_node1737494739792 = DropFields.apply(frame=Joinwithtracks_node1737494696299, paths=["id", "`.track_id`"], transformation_ctx="DropFields_node1737494739792")

# Script generated for node Destination
EvaluateDataQuality().process_rows(frame=DropFields_node1737494739792, ruleset=DEFAULT_DATA_QUALITY_RULESET, publishing_options={"dataQualityEvaluationContext": "EvaluateDataQuality_node1737494526527", "enableDataQualityResultsPublishing": True}, additional_options={"dataQualityResultsPublishing.strategy": "BEST_EFFORT", "observations.scope": "ALL"})
Destination_node1737494758812 = glueContext.write_dynamic_frame.from_options(frame=DropFields_node1737494739792, connection_type="s3", format="glueparquet", connection_options={"path": "s3://project-spotify-etl-bucket/datawarehouse/", "partitionKeys": []}, format_options={"compression": "snappy"}, transformation_ctx="Destination_node1737494758812")

job.commit()