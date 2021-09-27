import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo14-addons-oca-wms",
    description="Meta package for oca-wms Odoo addons",
    version=version,
    install_requires=[
        'odoo14-addon-delivery_carrier_preference',
        'odoo14-addon-delivery_carrier_warehouse',
        'odoo14-addon-sale_stock_available_to_promise_release',
        'odoo14-addon-shopfloor',
        'odoo14-addon-shopfloor_base',
        'odoo14-addon-shopfloor_checkout_sync',
        'odoo14-addon-shopfloor_example',
        'odoo14-addon-shopfloor_mobile',
        'odoo14-addon-shopfloor_mobile_base',
        'odoo14-addon-shopfloor_packing_info',
        'odoo14-addon-shopfloor_workstation',
        'odoo14-addon-shopfloor_workstation_mobile',
        'odoo14-addon-stock_available_to_promise_release',
        'odoo14-addon-stock_available_to_promise_release_dynamic_routing',
        'odoo14-addon-stock_checkout_sync',
        'odoo14-addon-stock_dynamic_routing',
        'odoo14-addon-stock_dynamic_routing_reserve_rule',
        'odoo14-addon-stock_move_source_relocate',
        'odoo14-addon-stock_move_source_relocate_dynamic_routing',
        'odoo14-addon-stock_picking_completion_info',
        'odoo14-addon-stock_picking_consolidation_priority',
        'odoo14-addon-stock_picking_type_shipping_policy',
        'odoo14-addon-stock_picking_type_shipping_policy_group_by',
        'odoo14-addon-stock_reception_screen',
        'odoo14-addon-stock_storage_type',
        'odoo14-addon-stock_storage_type_buffer',
        'odoo14-addon-stock_storage_type_putaway_abc',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
    ]
)
