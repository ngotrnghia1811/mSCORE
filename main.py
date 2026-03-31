import os, json, sys

def main(config):
    
    from modules.skill_reason import SkillReason
    skill_reason = SkillReason(**config, config=config)

    if 'train' in config:
        skill_reason.train()
    if 'dataset_split' in config:
        dataset_split = config['dataset_split']
    else:
        dataset_split = 'dev'
    skill_reason.eval(dataset_split=dataset_split)

if __name__ == "__main__":
    set_start_method("spawn")
    main()