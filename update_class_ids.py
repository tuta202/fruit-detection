import os

def update_class_ids(label_folder, old_id, new_id):
    for dirpath, _, filenames in os.walk(label_folder):
        for filename in filenames:
            if not filename.endswith('.txt'):
                continue
                
            # if not filename.startswith('tomato'):
            #     continue

            file_path = os.path.join(dirpath, filename)

            with open(file_path, 'r') as f:
                lines = f.readlines()

            updated_lines = []
            for line in lines:
                parts = line.strip().split()
                if len(parts) < 5:
                    continue  # bỏ qua dòng lỗi

                if parts[0] == str(old_id):
                    parts[0] = str(new_id)
                updated_lines.append(' '.join(parts) + '\n')

            with open(file_path, 'w') as f:
                f.writelines(updated_lines)

    print(f"✅ Successfully updated class_id from {old_id} to {new_id} in {label_folder}")

update_class_ids('datasets/fruit/train/labels', 0, 7)
update_class_ids('datasets/fruit/valid/labels', 0, 7)
update_class_ids('datasets/fruit/test/labels', 0, 7)