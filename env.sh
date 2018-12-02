export SOURCE_DIR=`pwd`
export WORK_DIR=${SOURCE_DIR}/work
export IMAGE_DIR=${SOURCE_DIR}/images
export TEST_IMAGE_DIR=${SOURCE_DIR}/test_images
export ANNOTATION_DIR=${SOURCE_DIR}/annotation

export TRAIN_DIR=${WORK_DIR}/train
export EXPORTED_MODEL_DIR=${WORK_DIR}/exported_model

export MODELS_DIR=${WORK_DIR}/models
export RESEARCH_DIR=${MODELS_DIR}/research

export PYTHONPATH=${RESEARCH_DIR}:${RESEARCH_DIR}/slim
