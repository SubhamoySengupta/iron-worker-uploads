import hyve
import sys

input_params = hyve.input_params.get_credentials()


# for local testing use this iron payload list
# sys.argv = [
# 				'main.py',
# 				'-d',
# 				'/mnt/task/',
# 				'-e',
# 				'production',
# 				'-id',
# 				'55094fe1f3b9954248001453',
# 				'-payload', 'task_payload.json'
# 			]

input_params.update(hyve.input_params.get_data_from_payload(sys.argv))

aws_conn = hyve.aws_connection.connect_S3(input_params)

aws_conn.connect_to_aws_bucket(input_params['bucket'])

aws_conn.download_file(input_params)

new_image = hyve.tweak_pic.image_resizer(input_params['image_name'])

new_image.resize(input_params)

aws_conn.upload_files(input_params)

print '~~The END~~'
