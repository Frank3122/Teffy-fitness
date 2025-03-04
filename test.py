



from teffyapp.models import PersonalInformation, AddMember

   
lead = PersonalInformation.objects.get(id=65)
    if not lead.converted_member:
    last_member = AddMember.objects.order_by('-id').first()

    if last_member and last_member.member_id:
    last_id = int(last_member.member_id.replace("TFM", ""))
    else:
    last_id = 0  # Start from TFM1 if no members exist

    new_member_id = f"TFM{last_id + 1}"

    # Create a new AddMember entry
    new_member = AddMember.objects.create(
    member_id=new_member_id,
    name=lead.name,
    gender=lead.gender,
    mobile_number=lead.mobile_number,
    email=lead.email,
    converted_from_lead=lead  # Link lead to this member
    )

    # Link the member back to the lead
    lead.converted_member = new_member
    lead.save()

    print(f"✅ Lead {lead.name} converted to Member {new_member.member_id}")

    else:
    print("❌ This lead is already linked to a member.")




from teffyapp.models import PersonalInformation, AddMember
lead = PersonalInformation.objects.get(id=65)
if not lead.converted_member:
    last_member = AddMember.objects.order_by('-id').first()
    if last_member and last_member.member_id:
        last_id = int(last_member.member_id.replace("TFM", ""))
    else:
        last_id = 0  
    new_member_id = f"TFM{last_id + 1}"
    new_member = AddMember.objects.create(
        member_id=new_member_id,
        name=lead.name,
        gender=lead.gender,
        mobile_number=lead.mobile_number,
        email=lead.email,
        converted_from_lead=lead
    )
    lead.converted_member = new_member
    lead.save()
    print("Lead", lead.name, "has been successfully converted to Member", new_member.member_id)
else:
    print("This lead is already linked to a member.")
