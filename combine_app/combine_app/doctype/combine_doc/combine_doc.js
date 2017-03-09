// Copyright (c) 2016, korecent and contributors
// For license information, please see license.txt

frappe.ui.form.on('Combine Doc', {
	refresh: function(frm) {

	}
});

function cal (frm, doc) {
	var total_amount = 0;
	var grand_total = 0;
	var len =  frm.doc.outstanding_invoices ? frm.doc.outstanding_invoices.length : 0
	if(len)
	{
		for (var i = 0;i<len;i++)
		{
			grand_total  += cint(frm.doc.outstanding_invoices[i].total_amount); 
			total_amount += cint(frm.doc.outstanding_invoices[i].outstanding_amount);
		}
	}
	frappe.model.set_value("Combine Doc",frm.docname, "total_amount",total_amount);
	frappe.model.set_value("Combine Doc",frm.docname, "grand_total", grand_total);
}


frappe.ui.form.on("Combine Doc",{onload:function(frm, doc){
		cal(frm,doc);
		var total_amount = cint(frm.doc.total_amount);
		if(total_amount == 0 ){
			frappe.model.set_value("Combine Doc",frm.docname,"status","Settled");
		}
		else{
			frappe.model.set_value("Combine Doc",frm.docname,"status","Due for Payment");
		}
	}
});


frappe.ui.form.on("Combine Doc Detail",{"outstanding_invoices_remove" : function(frm ,doc){
		cal(frm,doc);
	}
});
